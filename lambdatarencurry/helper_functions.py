"""
This contains the functions for Module 1 assignment. A number of basic helper
functions to practice on.
"""
import pandas as pd


class DataFrameHelper:
    """
    Class created for helper methods on which act on Dataframes.
    """
    def __init__(self, df):
        self.df = df

    def null_count(self):
        """
        Check a dataframe for nulls and return the number of missing values.
        """
        return self.df.isnull().sum().sum()

    def train_test_split(self, frac):
        """
        A Train/Test split function for a dataframe that returns both the
        Training and Testing sets. Frac refers to the percent of data you
        would like to set aside for Training.
        """

        # Retrieve the length of the dataframe and calculate the length of
        # the 'frac' for Training data (train_length)
        df_length = len(self.df)
        train_length = int(round(df_length * frac, 0))

        # Split the dataframe into Train and Test based on the train_length
        df_train = self.df.iloc[:train_length]
        df_test = self.df.iloc[train_length:]

        return df_train, df_test

    def randomize(df):
        """
        Randomization function that randomizes all of a dataframes cells
        then returns that randomized dataframe.
        """
        df = df.copy()
        # Use the pandas built in `sample()` function to create the randomize
        df_results = df.sample(frac=1)

        return df_results

    # def rm_outlier(df):
    #     """
    #     A 1.5*Interquartile range outlier detection/removal function that
    #     gets rid of outlying rows and returns that outlier cleaned dataframe.
    #     """
    #     # TODO - Implement
    #     return 'rm_outlier'

    # def list_2_series(list_2_series, df):
    #     """
    #     Single function to take a list and dataframe then turn the list into
    #     a series and add it to the inputted dataframe as a new column.
    #     """
    #     # TODO - Implement
    #     return 'list_2_series'


class SeriesHelper:
    def __init__(self, series):
        self.series = series

    def split_dates(date_series):
        """
        Function to split dates of format "MM/DD/YYYY" into multiple columns
        (df['month'], df['day'], df['year']) and then return the same dataframe
        with those additional columns.
        """
        # Make a copy of our Series to work on in this function.
        date_series = date_series.copy()

        # Create an empty dataframe to add the split dates to and return
        df_results = pd.DataFrame()

        # Ensure that the Series is a DateTime datatype and not other datatypes
        try:
            date_series = pd.to_datetime(date_series)
        except Exception:
            print('Please make sure that the Series passed is only dates.')
            return

        # Assign the Date Parts to new columns in the result dataframe.
        df_results['month'] = date_series.dt.month
        df_results['day'] = date_series.dt.day
        df_results['year'] = date_series.dt.year

        return df_results

    # def addy_split(add_series):
    #     """
    #     Splits addresses into three columns (df['city'], df['state'],
    #     and df['zip'])
    #     """
    #     # TODO - Implement
    #     return 'addy_split'
    #
    # def abbr_2_st(state_series, abbr_2_state=True):
    #     """
    #     Return a new column with the full name from a State abbreviation column
    #     -> An input of FL would return Florida. This function should also take
    #     a boolean (abbr_2_state) and when False takes full state names and
    #     return state abbreviations. -> An input of Florida would return Fl.
    #     """
    #     # TODO - Implement
    #     return 'abbr_2_st'
