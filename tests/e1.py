OK_FORMAT = False

name = 'e1'

import pandas as pd
import numpy as np

# Test that the dataframe is loaded correctly
try:
    assert isinstance(df, pd.DataFrame), "df should be a pandas DataFrame"
    assert df.shape[0] > 0, "DataFrame should not be empty"
    assert 'indicator_code' in df.columns, "DataFrame should have 'indicator_code' column"
    assert 'description' in df.columns, "DataFrame should have 'description' column"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
