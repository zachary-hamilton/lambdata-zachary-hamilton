import unittest
import pandas as pd
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import list_to_column
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import split_dates
from lambdata_zachary_hamilton.lambdata_zachary_hamilton import Column



class TestWranglingFunctions(unittest.TestCase):

    def test_list_to_column(self):
        df = pd.DataFrame({'a':[1,2,3]})
        lst = ['2020-5-6', '2020-12-25']

        df = list_to_column(df, lst, 'dates')
        
        # testing the column names
        self.assertEqual(df.columns[0], 'a')
        self.assertEqual(df.columns[1], 'dates')

        self.assertEqual(df.iloc[0][0], 1)
        self.assertEqual(df.iloc[0][1], '2020-5-6')


if __name__ == '__main__':
    unittest.main()
    