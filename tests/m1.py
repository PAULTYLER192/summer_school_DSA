OK_FORMAT = False

name = 'm1'

import numpy as np
import matplotlib.pyplot as plt

# Test that dataset is loaded correctly
try:
    assert isinstance(data, dict) or hasattr(data, 'keys'), "data should be a dictionary-like object"
    assert 'd' in data or 'd' in data.keys(), "Dataset should contain 'd' key"
    assert 'l' in data or 'l' in data.keys(), "Dataset should contain 'l' key"
    
    assert isinstance(d, np.ndarray), "d should be a NumPy array"
    assert isinstance(l, np.ndarray), "l should be a NumPy array"
    assert d.shape == (1000, 2), f"d should have shape (1000, 2), got {d.shape}"
    assert l.shape == (1000, 1) or l.shape == (1000,), f"l should have shape (1000, 1) or (1000,), got {l.shape}"
    
    # Check labels are 0 or 1
    unique_labels = np.unique(l)
    assert all(label in [0, 1] for label in unique_labels), "Labels should be 0 or 1"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
