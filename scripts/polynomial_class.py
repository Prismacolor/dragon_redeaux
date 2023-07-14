"""Script for building Polynomial classification model"""
import matplotlib as plt
import numpy as np
import pandas as pd

from utils.helper import create_main_dataframe


def main():
    """
    main function for processing data and building/training model
    :param: none
    :return: none
    """
    # concatenate data into single dataframe
    main_df = create_main_dataframe()
    print(main_df.head())
    
    # shuffle data
    main_df.sample(frac=1).reset_index(drop=True)

    # begin preprocessing data
    y = main_df['species']
    main_df.drop(['species'])

    # TODO preprocess the data using helper function


if __name__ == '__main__':
    main()
