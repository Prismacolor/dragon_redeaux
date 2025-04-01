import pickle
import os


def test_model_loading():
    model_path = "C:/Users/noell/programming_projects/dragon_redeaux/dragon_models"

    print(f"Checking if file exists: {os.path.exists(model_path)}")

    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("Successfully loaded model!")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False


if __name__ == "__main__":
    test_model_loading()