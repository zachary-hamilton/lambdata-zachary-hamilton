import pandas as pd
import numpy as np


def list_to_column(df, lst, column_name):
    '''
    This function takes a list and adds it as a new column of
    a dataframe
    '''

    # turns the original list into a series
    my_series = pd.Series(lst)

    # adding the series to the dataframe
    df = pd.concat([df, my_series], axis=1)

    # renaming the column headers
    columns = df.columns.tolist()
    columns.append(column_name)
    df.columns = columns
    return df


def split_dates(df, column, year=True, month=True,
                day=True, weekday=True, replace=True):
    '''
    This function will take a dataframe column that is a date and split it into its
    comoponent parts
    '''

    df = df.copy()

    # turning the values in the columns into datetime format
    df[column] = df[column].apply(
        lambda x: pd.to_datetime(
            x, infer_datetime_format=True))     

    # these if statements display the designated date data
    if year:
        df['year'] = df[column].apply(lambda x: x.year)
    if month:
        df['month'] = df[column].apply(lambda x: x.month)
    if day:
        df['day'] = df[column].apply(lambda x: x.day)
    if weekday:
        df['weekday'] = df[column].apply(lambda x: x.weekday())

    # this will remove the original column if desired
    if replace:
        df = df.drop(columns=[column])

    return df
