import pandas as pd


def count_nan_in_cols(df):
    return df.isnull().sum()
