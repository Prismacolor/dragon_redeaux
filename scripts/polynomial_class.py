import matplotlib as plt
import numpy as np
import pandas as pd

from utils.helper import create_main_dataframe


def main():
    main_df = create_main_dataframe()
    print(main_df.head())


if __name__ == '__main__':
    main()
