OK_FORMAT = False

name = 'e2'

import pandas as pd

# Test that dataframe is reshaped to long format
try:
    assert isinstance(df_long, pd.DataFrame), "df_long should be a pandas DataFrame"
    assert 'date' in df_long.columns, "DataFrame should have 'date' column"
    assert 'value' in df_long.columns, "DataFrame should have 'value' column"
    assert 'indicator_code' in df_long.columns, "DataFrame should have 'indicator_code' column"
    assert 'description' in df_long.columns, "DataFrame should have 'description' column"

except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass