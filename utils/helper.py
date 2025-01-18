"""helper functions"""
import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder


columns = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings', 'est_body_length',
           'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture', 'snout_length',
           'shape_of_body', 'wingspan', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
           'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'aggressiveness', 'flight_speed', 'is_venomous',
           'breathing_fire_observed',  'observed_by', 'year_observed', 'species']


def create_main_dataframe():
    """
    function to pull in data and concatenate into larger dataframe
    :params: none
    :return: main dataframe
    """
    dfs = []

    directory = r"..\data\dragon_spreadsheets"
    csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

    for file in csv_files:
        file_str = directory + r'\{}'.format(file)
        df = pd.read_csv(file_str, index_col=False)
        dfs.append(df)

    # Save the DataFrame as a CSV file
    main_df = pd.concat(dfs, axis=0)
    main_df.to_csv('../data/full_data.csv', index=False)

    return main_df


def preprocess_data(df, encoded_labels):
    """
    preprocess data in main dataframe
    :param: df
    :return: dataframe df, series labels
    """
    # drop columns that aren't needed and shuffle data
    df = df.drop(['observed_by', 'year_observed'], axis=1)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df['species'] = df['species'].map(encoded_labels)

    # secure the labels
    labels = df['species']
    df.drop(['species'], axis=1)

    # scale the numerical data and encode categorical data
    numerical_columns = [
        'est_body_length', 'wingspan', 'flight_speed', 'number_of_limbs', 'snout_length',
        'aggressiveness'
        ]
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    categorical_features = ['gender', 'estimated_age', 'color_of_scales', 'color_of_eyes', 'color_of_wings',
     'shape_of_snout', 'shape_of_teeth', 'scales_present', 'scale_texture', 'body_texture',
     'shape_of_body', 'number_of_limbs', 'facial_spikes', 'frilled', 'length_of_horns',
     'shape_of_horns', 'shape_of_tail', 'loc_of_sighting', 'is_venomous',
     'breathing_fire_observed']
    encoder = OneHotEncoder()
    encoded_features = encoder.fit_transform(df[categorical_features]).toarray()
    df_encoded = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))
    df = pd.concat([df, df_encoded], axis=1)
    df = df.drop(categorical_features, axis=1)

    return df, labels


def numerical_labels_to_categories(y, reverse_labels):
    df = pd.DataFrame({'labels': y})
    df['labels'] = df['labels'].map(reverse_labels)

    return df['labels']

