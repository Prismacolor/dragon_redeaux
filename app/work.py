import pickle
import os
import joblib


def load_model(model_type):
    """
    Load the model based on the model_type.
    :params: model_type (str): Type of model to load
    :return: Loaded machine learning model or None
    """
    model_filename = f"{model_type}_model.joblib"

    current_file = os.path.abspath(__file__)
    print(f"Current file path: {current_file}")

    app_dir = os.path.dirname(current_file)
    print(f"App directory: {app_dir}")

    project_root = os.path.dirname(app_dir)
    print(f"Project root: {project_root}")

    models_dir = os.path.join(project_root, "dragon_models")
    print(f"Models directory: {models_dir}")
    print(f"Models directory exists: {os.path.exists(models_dir)}")

    model_path = os.path.join(models_dir, model_filename)
    print(f"Looking for model at: {model_path}")
    print(f"Model file exists: {os.path.exists(model_path)}")

    # List all files in the models directory to confirm what's there
    if os.path.exists(models_dir):
        print(f"Files in models directory: {os.listdir(models_dir)}")

    try:
        if not os.path.exists(model_path):
            print(f"Model file {model_filename} not found")
            return None, 'File Not Found'

        app_model = joblib.load(model_path)
        print(f"Model loaded successfully")
        return app_model, 'ok'

    except FileNotFoundError:
        print(f"Model file {model_filename} not found")
        return None, 'File Not Found'

    except Exception as e:
        print(f"Error loading model: {str(e)}")
        import traceback
        traceback.print_exc()  # Print full traceback
        return None, f'Could not load model: {str(e)}'

if __name__ == "__main__":
    load_model('neuralnet')