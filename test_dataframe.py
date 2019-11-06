"""
Usage: test_dataframe.py
"""
## data is at: https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD

import pandas as pd

# function creating pandas dataframe
def create_dataframe(url):
    '''
    Creates a pandas dataframe.
    :param str url:
    :returns dataframe:
    '''
    data_frame = pd.read_csv(url)
    return data_frame

# test the dataframe created
def test_create_dataframe(url, column_names):
    '''
    Applys rules to the dataframe
    :param df: pandas dataframe to be checked
    :param column_names: list of names
    '''
    data_frame = create_dataframe(url)
    column_names = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']

    # check unknown columns names
    for col in data_frame.columns.values.tolist():
        assert col in column_names

    # check values in column have same type
    row_count = 0
    for col in column_names:
        # look at df[col]
        for element in data_frame[col]:
            if row_count == 0:
                continue
            assert type(element) == type(data_frame[col][0])
            row_count += 1

    # check number of rows in dataframe
    assert data_frame.shape[0] >= 10

    # Check that all columns have values of the corect type.
    row_count = 0
    for col in column_names:
        # look at df[col]
        for element in data_frame[col]:
            if row_count == 0:
                pass
            else:
                if type(element) == type(data_frame[col][0]):
                    break
                row_count += 1
    assert row_count < data_frame.shape[0]

    # check for null values
    assert not data_frame.isnull().values.any()

    # check dataframe has at least one row
    assert data_frame.shape[0] > 1

    # if nothing happens, df passes the test
    return True
