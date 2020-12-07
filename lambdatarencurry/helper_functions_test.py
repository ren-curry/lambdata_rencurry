import unittest
import pandas as pd
import numpy as np
from helper_functions import DataFrameHelper, SeriesHelper


class HelperFunctionsTest(unittest.TestCase):
    """Unit Test Cases for helper_functions module"""

    def test_null_count(self):
        """Test that DataFrameHelper.null_count() returns total null cells"""
        df_test1 = pd.DataFrame([
                        [1, np.nan, 1],
                        [np.nan, 1, 1],
                        [1, 1, np.nan]
                       ])
        df_test2 = pd.DataFrame([
                        [1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]
                       ])

        dfh_test1 = DataFrameHelper(df_test1)
        dfh_test2 = DataFrameHelper(df_test2)

        self.assertEqual(dfh_test1.null_count(), 3)
        self.assertEqual(dfh_test2.null_count(), 0)

    def test_train_test_split(self):
        """
        Test that DataFrameHelper.train_test_split() returns two dataframes
        with the appropriate fraction of the original dataframe
        """

        df_original = pd.DataFrame(
                                   np.random.randint(
                                                     0,
                                                     100,
                                                     size=(10, 4)),
                                   columns=list('ABCD'))

        frac = 0.8
        length_original = len(df_original)
        dfh_orginal = DataFrameHelper(df_original)

        df_train, df_test = dfh_orginal.train_test_split(frac)

        self.assertEqual((len(df_train) + len(df_test)), length_original)
        self.assertEqual(len(df_train), (length_original * frac))
        self.assertEqual(len(df_test), (length_original
                                        - (length_original * frac)))

    def test_randomize(self):
        """
        Test that the DataFrame.randomize() returns a dataframe not
        matching the original
        """

        df_original = pd.DataFrame(
                                   np.random.randint(
                                                     0,
                                                     100,
                                                     size=(10, 4)),
                                   columns=list('ABCD'))

        dfh_test1 = DataFrameHelper(df_original)
        dfh_test1.randomize()

        pd.testing.assert_frame_equal(df_original, dfh_test1.df)


if __name__ == "__main__":
    unittest.main()
