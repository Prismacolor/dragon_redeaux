"""Script for building Polynomial classification model"""
import numpy as np
import pandas as pd
import sklearn as sk

from utils.helper import create_main_dataframe, preprocess_data


def main():
    """
    main function for processing data and building/training model
    :param: none
    :return: none
    """
    # concatenate data into single dataframe
    main_df = create_main_dataframe()
    print(main_df.head())

    # get features and labels
    x, y = preprocess_data(main_df)


if __name__ == '__main__':
    main()
