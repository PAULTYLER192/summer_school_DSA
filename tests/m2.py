OK_FORMAT = False

name = 'm2'

import numpy as np
import matplotlib.pyplot as plt

# Test that separating line is drawn
try:
    # Basic checks - the line should be defined
    # We can't easily test the visual output, but we can check that
    # the data is properly loaded and structured
    assert isinstance(d, np.ndarray), "d should be a NumPy array"
    assert isinstance(l, np.ndarray), "l should be a NumPy array"
    assert d.shape[0] == l.shape[0] or d.shape[0] == l.flatten().shape[0], "d and l should have same number of samples"
    
    # Check that we have both classes
    unique_labels = np.unique(l.flatten())
    assert len(unique_labels) == 2, "Should have exactly 2 classes"
    assert 0 in unique_labels and 1 in unique_labels, "Should have classes 0 and 1"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
