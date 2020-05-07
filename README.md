# lambdata-zachary-hamilton

## Installation

TODO

## Usage

```py
import pandas as pd
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import list_to_column
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import split_dates

df = pd.DataFrame({'a':[1,2,3]})

lst = ['2020-5-6', '2020-12-25']

df = list_to_column(df, lst, 'dates')
print(df)

df = split_dates(df, 'dates')
print(df)
```