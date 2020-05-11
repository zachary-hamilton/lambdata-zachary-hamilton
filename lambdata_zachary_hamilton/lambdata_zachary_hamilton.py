import pandas as pd
import numpy as np


def list_to_column(df, lst, column_name):
    '''
    This function takes a list and adds it as a new column of
    a dataframe
    '''
    my_series = pd.Series(lst)

    columns = df.columns.tolist()
    columns.append(column_name)

    df = pd.concat([df, my_series], axis=1)
    df.columns = columns
    return df


def split_dates(df, column, year=True, month=True,
                day=True, weekday=True, replace=True):
    '''
    This function will take a dataframe column that is a date and split it into its
    comoponent parts
    '''

    df[column] = df[column].apply(
        lambda x: pd.to_datetime(
            x, infer_datetime_format=True))

    if year:
        df['year'] = df[column].apply(lambda x: x.year)

    if month:
        df['month'] = df[column].apply(lambda x: x.month)

    if day:
        df['day'] = df[column].apply(lambda x: x.day)

    if weekday:
        df['weekday'] = df[column].apply(lambda x: x.weekday())

    if replace:
        df = df.drop(columns=[column])

    return df
