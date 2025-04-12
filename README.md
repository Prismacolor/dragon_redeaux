# Model Training and Prediction API

A complete machine learning pipeline for generating synthetic data, training multiple model types, and serving predictions via a Flask API.

## Project Overview

This project demonstrates a full machine learning workflow:
1. **Data Generation**: Create synthetic datasets for training and testing
2. **Data Preprocessing**: Functions for cleaning and preprocessing training data and prediction inputs
2. **Model Training**: Build and train either polynomial regression or neural network models
3. **API Deployment**: Serve model predictions through a Flask REST API

Note on data generation ::: this was a challenge. Initial efforts to generate dragon data resulted in perfectly collinear data which 
led to the model always getting 1.0 (100%) accuracy even on validation and test sets. I initially tried to correct ths by sending my 
test scripts through Anthropic's Claude Sonnet to add some variance to my data scripts. However, I soon discovered that the variability
was being added in the same formulaic way for every species, meaning that the data remained perfectly collinear. To muddy things up, I
created more overlapping locations, removed locations that would clearly give away a species, and messed with the distributions so that 
no two species had the same distribution of numerical data. I also varied the number of specimens for each species to create some class 
imbalance. It is not perfect, (given that dragons are not real, how can it be?) but it at least somewhat simulates casual observations. 
There are also code outs for "missing data", maybe something did not get recorded properly or could not be determined during the initial 
observation. There are also code outs for things like missing limbs and wings (because sometimes dragons choose violence.) So a fun thought
exercise for any ML/DS practitioner may be to see how they can muddy up the data further. I toyed with removing some of the features but that
means you will have to do some further changes up stream (like when you preprocess the prediction data. I did finally get some variance and 
the model actually began a legitimate training arc and the final results for the test set were 98-99% accuracy with 0.04 loss. Still a little 
too high but I am very happy with the fact that I got an actual training arc to go. 

## Project Structure

```
dragon_redeaux/
│
├── api_model_classes/         # Core model class definitions
│   ├── __init__.py
│   ├── neuralnetmodel.py      # Neural network model implementation
│   └── polynomial_model.py    # Polynomial model implementation
│
├── app/                       # Flask API application
│   ├── __init__.py
│   ├── .env                   # Environment variables for the app
│   └── dragon_app.py          # Main Flask application
│
├── data/                      # Data storage
│   ├── dragon_data_scripts/   # Scripts for data creation
│   ├── dragon_plots/          # Generated plots and visualizations
│   ├── dragon_spreadsheets/   # CSVs with training data
│   ├── __init__.py
│   └── full_data.csv          # Main dataset
│
├── dragon_models/             # Saved model files
│   ├── __init__.py
│   ├── neuralnet_model.joblib # Saved neural network model
│   └── onehot_encoder.joblib  # Encoder for categorical variables
│
├── scripts/                   # Main scripts
│   ├── __init__.py
│   ├── create_data_sheets.py  # Data generation script
│   ├── neuralnet_script.py    # Script to train neural network
│   └── polynomial_script.py   # Script to train polynomial model
│
├── tests/                     # Test files
│   ├── __init__.py
│   └── test_functions.py      # Test functions
│
├── utils/                     # Utility modules
│   ├── __init__.py
│   └── helper.py              # Helper functions
│
├── .gitignore                 # Git ignore file
├── Dockerfile                 # Docker configuration
├── logger.py                  # Logging utility 
├── README.md                  
└── requirements.txt           # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
   ```
   https://github.com/Prismacolor/dragon_redeaux.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
4. Add .env:
    you will need to add a .env file to the app folder with the MODEL_TYPE parameter (plus any other parameters you want to add)

## Data Generation

Generate synthetic datasets with the data creation script:

```bash
python scripts/create_data_sheets.py 
```

## Model Training

Train either a polynomial regression or neural network model:

### Polynomial Regression

```bash
python scripts/polynomial_script.py 
```

### Neural Network

```bash
python scripts/neuralnet_script.py 
```

## Running the API

Start the Flask API server:

```bash
cd app
python dragon_app.py
```

The API will be available at `http://localhost:8080`.

You can also run the application using Docker:

```bash
docker docker build -t dragon-classifier .
docker run -p 8080:8080 dragon-classifier
```

## API Usage

### Making Predictions

To get predictions from a trained model, send a POST request via Postman to the `/predict` endpoint:

Sample Configuration:
- Method: POST
- URL: http://localhost:8080/predict
- Headers: Content-Type: application/json
- Body (raw JSON):
  ```json
  {
    "gender": "male",
    "estimated_age": "juvenile",
    "color_of_scales": "grey",
    "color_of_eyes": "blue",
    "color_of_wings": "grey",
    "est_body_length": 4,
    "shape_of_snout": "snub",
    "shape_of_teeth": "pointed",
    "scales_present": "yes",
    "feathers_present": "no",
    "scale_texture": "smooth",
    "body_texture": "scaled",
    "snout_length": 0.75,
    "shape_of_body": "lithe",
    "wingspan": 6,
    "number_of_limbs": 2,
    "facial_spikes": "no",
    "frilled": "no",
    "length_of_horns": "short",
    "shape_of_horns": "twisted",
    "shape_of_tail": "pointed",
    "loc_of_sighting": "Peru",
    "aggressiveness": 7,
    "flight_speed": 65,
    "is_venomous": "yes",
    "breathing_fire_observed": "no",
    "breathing_ice_observed": "no",
    "observed_by": "TNR",
    "year_observed": 2022
}
  ```

### API Response

The API will respond with a JSON object containing the prediction:

```json
{
  "prediction": "SomeDragon",
  "input_data": {
    "gender": "male",
    "estimated_age": "juvenile",
    "color_of_scales": "grey",
    "color_of_eyes": "blue",
    "color_of_wings": "grey",
    "est_body_length": 4,
    "shape_of_snout": "snub",
    "shape_of_teeth": "pointed",
    "scales_present": "yes",
    "feathers_present": "no",
    "scale_texture": "smooth",
    "body_texture": "scaled",
    "snout_length": 0.75,
    "shape_of_body": "lithe",
    "wingspan": 6,
    "number_of_limbs": 2,
    "facial_spikes": "no",
    "frilled": "no",
    "length_of_horns": "short",
    "shape_of_horns": "twisted",
    "shape_of_tail": "pointed",
    "loc_of_sighting": "Peru",
    "aggressiveness": 7,
    "flight_speed": 65,
    "is_venomous": "yes",
    "breathing_fire_observed": "no",
    "breathing_ice_observed": "no",
    "observed_by": "TNR",
    "year_observed": 2022
    }
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.