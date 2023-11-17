import numpy as np
#import pandas as pd

def encode_cyclical_feature(input_df, output_df, column, period):
    """ Encodes cyclical features to sine and cosine

    Args:
        input_df (DataFrame): The input data frame
        output_df (DataFrame): The output data frame
        column (str): The feature to encode
        period (int64): The cycle duration
    """
    sin_values = np.sin(2 * np.pi * input_df[column] / period)
    cos_values = np.cos(2 * np.pi * input_df[column] / period)

    output_df[column + '_sin'] = sin_values
    output_df[column + '_cos'] = cos_values
    #position = df.columns.get_loc(column) + 1
    #df.insert(position, column + '_sin', sin_values)
    #df.insert(position + 1, column + '_cos', cos_values)
    # df.drop(column, axis=1, inplace=True)