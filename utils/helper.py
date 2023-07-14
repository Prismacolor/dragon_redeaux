"""helper functions"""
import os
import pandas as pd

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

    directory = r"C:\Users\noell\PycharmProjects\dragon_redeaux\data\dragon_spreadsheets"
    csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

    for file in csv_files:
        file_str = directory + r'\{}'.format(file)
        df = pd.read_csv(file_str, index_col=False)
        main_df = pd.concat([main_df, df], axis=0)

    return main_df


def preprocess_data(df):
    """
    preprocess data in main dataframe
    :param df:
    :return: modified dataframe, encoded labels
    """

    df.drop(['observed_by', 'year_observed'], axis=1)

