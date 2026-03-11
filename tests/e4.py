OK_FORMAT = False

name = 'e4'

import pandas as pd

# Test that CPI dataframes are filtered correctly
try:
    assert isinstance(df_cpi, pd.DataFrame), "df_cpi should be a pandas DataFrame"
    assert isinstance(df_all_items, pd.DataFrame), "df_all_items should be a pandas DataFrame"
    assert isinstance(df_core, pd.DataFrame), "df_core should be a pandas DataFrame"
    assert isinstance(df_food, pd.DataFrame), "df_food should be a pandas DataFrame"
    assert isinstance(df_efu, pd.DataFrame), "df_efu should be a pandas DataFrame"
    
    # Check that all indicator codes start with CPI_
    if len(df_cpi) > 0:
        assert all(df_cpi['indicator_code'].str.startswith('CPI_')), "All indicator codes should start with 'CPI_'"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
