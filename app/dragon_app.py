import joblib
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import pandas as pd
import sys
from werkzeug.exceptions import InternalServerError
from logger import logger

# Setup project paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'utils'))
sys.path.append(os.path.join(project_root, 'api_model_classes'))

from utils.helper import preprocess_prediction_data

load_dotenv()

# Define species labels
encoded_labels = {
    'Amazonian Blue': 0,
    'Antipodean Opaleye': 1,
    'Canadian Sailwing': 2,
    'Chinese Fireball': 3,
    'Common Welsh Green': 4,
    'Egyptian Copperbelly': 5,
    'Hebridean Black': 6,
    'Hungarian Horntail': 7,
    'Kenyan Brushtail': 8,
    'Norwegian Ridgeback': 9,
    'Peruvian Vipertooth': 10,
    'Swedish Short Snout': 11,
    'Ukrainian Ironbelly': 12
}

reverse_labels = {v: k for k, v in encoded_labels.items()}
model_type = os.getenv("MODEL_TYPE")


def load_model(model_type):
    """
    Load the model based on the model_type.
    :params: model_type (str): Type of model to load
    :return: Loaded machine learning model or None
    """
    model_filename = f"{model_type}_model.joblib"

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(project_root, "dragon_models")

    try:
        app_model = joblib.load(os.path.join(models_dir, model_filename))
        logger.info(f"Successfully loaded model: {model_filename}")
        return app_model, 'ok'

    except FileNotFoundError:
        logger.error(f"Model file {model_filename} not found")
        return None, f'Model file {model_filename} not found'

    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return None, f"Error loading model: {e}"


app = Flask(__name__)


@app.route("/test", methods=["GET", "POST"])
def test_endpoint():
    """Simple test endpoint to confirm server is working"""
    if request.method == "POST":
        return jsonify({"message": "POST request received", "data": request.json})
    else:
        return jsonify({"message": "GET request received"})


@app.route("/predict/<model_type>", methods=["POST"])
def predict(model_type):
    """
    Prediction endpoint that takes input data from user
    :params: model_type: Type of model to use for prediction
    :returns: prediction result
    """
    model, status = load_model(model_type)

    if model is None:
        return jsonify({"error": f"Model {model_type} not loaded. Reason: {status}"}), 500

    try:
        input_data = request.json

        if not input_data:
            return jsonify({"error": "No input data provided"}), 400

        # Create input dictionary from the request data
        input_dict = {
            'gender': [input_data.get('gender')],
            'estimated_age': [input_data.get('estimated_age')],
            'color_of_scales': [input_data.get('color_of_scales')],
            'color_of_eyes': [input_data.get('color_of_eyes')],
            'color_of_wings': [input_data.get('color_of_wings')],
            'est_body_length': [input_data.get('est_body_length')],
            'shape_of_snout': [input_data.get('shape_of_snout')],
            'shape_of_teeth': [input_data.get('shape_of_teeth')],
            'scales_present': [input_data.get('scales_present')],
            'scale_texture': [input_data.get('scale_texture')],
            'body_texture': [input_data.get('body_texture')],
            'snout_length': [input_data.get('snout_length')],
            'shape_of_body': [input_data.get('shape_of_body')],
            'wingspan': [input_data.get('wingspan')],
            'number_of_limbs': [input_data.get('number_of_limbs')],
            'facial_spikes': [input_data.get('facial_spikes')],
            'frilled': [input_data.get('frilled')],
            'length_of_horns': [input_data.get('length_of_horns')],
            'shape_of_horns': [input_data.get('shape_of_horns')],
            'shape_of_tail': [input_data.get('shape_of_tail')],
            'loc_of_sighting': [input_data.get('loc_of_sighting')],
            'aggressiveness': [input_data.get('aggressiveness')],
            'flight_speed': [input_data.get('flight_speed')],
            'is_venomous': [input_data.get('is_venomous')],
            'breathing_fire_observed': [input_data.get('breathing_fire_observed')],
            'observed_by': [input_data.get('observed_by')],
            'year_observed': [input_data.get('year_observed')],
        }

        input_df = pd.DataFrame(input_dict)

        logger.info("Starting preprocessing")
        processed_df = preprocess_prediction_data(input_df)

        # Convert to numpy array for prediction
        processed_input = processed_df.values

        # Make prediction
        prediction_number = model.predict(processed_input)
        prediction_species = reverse_labels.get(prediction_number[0], "Unknown Species")

        # Return the prediction and input data as JSON
        return jsonify({
            "prediction": prediction_species,
            "input_data": input_data
        })

    except Exception as e:
        logger.exception(f"Error during prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run with debug=True to see detailed error messages
    app.run(host="0.0.0.0", port=8080, debug=True)