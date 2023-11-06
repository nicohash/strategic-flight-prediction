import numpy as np

def encode_cyclical_feature(df, column, period):
    """ Encodes cyclical features to sine and cosine

    Args:
        df (DataFrame): The input data frame
        column (int64): The feature to encode
        period (int64): The cycle duration
    """
    df[column + '_sin'] = np.sin(2 * np.pi * df[column] / period)
    df[column + '_cos'] = np.cos(2 * np.pi * df[column] / period)
    df.drop(column, axis=1, inplace=True)