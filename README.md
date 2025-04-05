TO do
6. refine readme
7. take one last stab at data issue: start with common welsh
8. final test of docker file

# Model Training and Prediction API

A complete machine learning pipeline for generating synthetic data, training multiple model types, and serving predictions via a Flask API.

## Project Overview

This project demonstrates a full machine learning workflow:
1. **Data Generation**: Create synthetic datasets for training and testing
2. **Model Training**: Build and train either polynomial regression or neural network models
3. **API Deployment**: Serve model predictions through a Flask REST API

## Project Structure

Based on the actual project files:

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
│   ├── dragon_data_scripts/   # Scripts for data manipulation
│   ├── dragon_plots/          # Generated plots and visualizations
│   ├── dragon_spreadsheets/   # Spreadsheet data files
│   ├── __init__.py
│   └── full_data.csv          # Main dataset
│
├── dragon_models/             # Saved model files
│   ├── __init__.py
│   ├── neuralnet_model.joblib # Saved neural network model
│   └── onehot_encoder.joblib  # Encoder for categorical variables
│
├── scripts/                   # Utility scripts
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
├── logger.py                  # Logging utility (at root level)
├── README.md                  # This file
└── requirements.txt           # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/model-training-api.git
   cd model-training-api
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

## Data Generation

Generate synthetic datasets with the data creation script:

```bash
# Generate data sheets
python scripts/create_data_sheets.py --samples 1000 --output data/dragon_spreadsheets/
```

## Model Training

Train either a polynomial regression or neural network model:

### Polynomial Regression

```bash
python scripts/polynomial_script.py --data data/full_data.csv --degree 3 --output dragon_models/
```

### Neural Network

```bash
python scripts/neuralnet_script.py --data data/full_data.csv --layers 3 --neurons 64 --epochs 100 --output dragon_models/
```

## Running the API

Start the Flask API server:

```bash
cd app
python dragon_app.py
```

The API will be available at `http://localhost:5000`.

You can also run the application using Docker:

```bash
docker build -t dragon-api .
docker run -p 5000:5000 dragon-api
```

## API Usage

### Making Predictions

To get predictions from a trained model, send a POST request to the `/predict` endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"model_type": "polynomial", "features": [1.2, 3.4, 2.1]}' http://localhost:5000/predict
```

Or use Postman with the following configuration:
- Method: POST
- URL: http://localhost:5000/predict
- Headers: Content-Type: application/json
- Body (raw JSON):
  ```json
  {
    "model_type": "neural_network",  // or "polynomial"
    "features": [1.2, 3.4, 2.1]
  }
  ```

### API Response

The API will respond with a JSON object containing the prediction:

```json
{
  "prediction": 42.56,
  "model_type": "neural_network",
  "timestamp": "2023-06-15T12:34:56.789Z"
}
```

## Configuration

The project uses a YAML configuration file (`config.yaml`) to set parameters for data generation and model training. You can edit this file to customize the behavior of the scripts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.