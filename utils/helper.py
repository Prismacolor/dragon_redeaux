"""helper functions"""
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

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
    main_df = pd.DataFrame(columns=columns)

    directory = r"..\data\dragon_spreadsheets"
    csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

    for file in csv_files:
        file_str = directory + r'\{}'.format(file)
        df = pd.read_csv(file_str, index_col=False)
        main_df = pd.concat([main_df, df], axis=0)

    # Save the DataFrame as a CSV file
    main_df.to_csv('../data/full_data.csv', index=False)

    return main_df


def preprocess_data(df, encoded_labels):
    """
    preprocess data in main dataframe
    :param: df
    :return: modified dataframe, encoded labels
    """
    # drop columns that aren't needed, shuffle data
    df.drop(['observed_by', 'year_observed'], axis=1)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df['species'] = df['species'].map(encoded_labels)

    # secure the labels
    labels = df['species']
    df.drop(['species'], axis=1)

    # scale the data
    # numerical_columns = ['aggressiveness', 'est_body_length', 'flight_speed', 'number_of_limbs', 'snout_length', 'wingspan']
    # scaler = StandardScaler()
    # df = scaler.fit_transform(df)

    # convert features to numerical features
    df = pd.get_dummies(df)

    return df, labels


def numerical_labels_to_categories(y, reverse_labels):
    df = pd.DataFrame({'labels': y})
    df['labels'] = df['labels'].map(reverse_labels)

    return df['labels']

