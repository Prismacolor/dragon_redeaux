import joblib
import pickle
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import uvicorn

from app_models import ModelInputs, PredictionResponse

load_dotenv()

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
    # models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dragon_models")

    current_file = os.path.abspath(__file__)
    app_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(app_dir)
    models_dir = os.path.join(project_root, "dragon_models")

    try:
        # model_path = os.path.join(models_dir, model_filename)
        app_model = joblib.load(os.path.join(models_dir, model_filename))

        return app_model, 'ok'

    except FileNotFoundError:
        print(f"Model file {model_filename} not found")
        return None, 'File Not Found'

    except Exception as e:
        print(f"Error loading model: {e}")  # TODO change this to logging
        return None, 'Could not load model'


app = FastAPI(
    title="Dragon Species Predictor",
    description="API for predicting dragon species given certain measurements",
    version="1.0.0"
)

model = load_model(model_type)

@app.post("/predict/{model_type}")
async def predict(input_data: ModelInputs):
    """
    Prediction endpoint that takes input data from user
    :params: input_data (object)
    :returns: prediction result
    """
    model, status = load_model(model_type)

    if model is None:
        raise HTTPException(status_code=500, detail=f"Model {model_type} not loaded. Re: {status}")

    try:
        input_list = [
            input_data.gender,
            input_data.estimated_age,
            input_data.color_of_scales,
            input_data.color_of_eyes,
            input_data.color_of_wings,
            input_data.est_body_length,
            input_data.shape_of_snout,
            input_data.shape_of_teeth,
            input_data.scales_present,
            input_data.scale_texture,
            input_data.body_texture,
            input_data.snout_length,
            input_data.shape_of_body,
            input_data.wingspan,
            input_data.number_of_limbs,
            input_data.facial_spikes,
            input_data.frilled,
            input_data.length_of_horns,
            input_data.shape_of_horns,
            input_data.shape_of_tail,
            input_data.loc_of_sighting,
            input_data.aggressiveness,
            input_data.flight_speed,
            input_data.is_venomous,
            input_data.breathing_fire_observed,
            input_data.observed_by,
            input_data.year_observed
        ]

        prediction_number = model.predict([input_list])
        prediction_species = reverse_labels.get(prediction_number[0], "Unknown Species")

        return PredictionResponse(
            prediction=prediction_species,
            input_data=input_data.model_dump()
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)