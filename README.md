# lambdata-zachary-hamilton

## Installation

```py
pip install -i https://test.pypi.org/simple/ lambdata-zachary-hamilton==2.0
```

## Usage

```py
import pandas as pd
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import list_to_column
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import split_dates
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import Column


df = pd.DataFrame({'a':[1,2,3]})
lst = ['2020-5-6', '2020-12-25']

# using the function to add a list to a dataframe
df = list_to_column(df, lst, 'dates')
print(df)

# using a function to split a column of dates into its components
# such as year, month, day
df = split_dates(df, 'dates')
print(df)

#using a class to add a list to a dataframe
my_column = Column(lst=lst, column_name='dates')
df = my_column.add_to_dataframe(df)
print(df)
```