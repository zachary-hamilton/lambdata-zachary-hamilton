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
    print(columns)
    
    df = pd.concat([df, my_series], axis=1)
    df.columns = columns
    print(df)
    return df


df = pd.DataFrame({'a': [1,2,3], 'b':[3,4,5]})
lst = [6,7]
list_to_column(df, lst, 'c')