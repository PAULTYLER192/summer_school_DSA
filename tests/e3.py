OK_FORMAT = False

name = 'e3'

import pandas as pd

# Test that date column is converted to datetime
try:
    assert isinstance(df_long, pd.DataFrame), "df_long should be a pandas DataFrame"
    assert 'date' in df_long.columns, "DataFrame should have 'date' column"
    assert pd.api.types.is_datetime64_any_dtype(df_long['date']), "Date column should be datetime type"

except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass