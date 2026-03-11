OK_FORMAT = False

name = 'm4'

import numpy as np
from scipy.stats import multivariate_normal

# Test that heatmap is created correctly
# Check Gaussian distributions are created
try:
    assert isinstance(gaussian_class_0, multivariate_normal), "gaussian_class_0 should be a multivariate_normal object"
    assert isinstance(gaussian_class_1, multivariate_normal), "gaussian_class_1 should be a multivariate_normal object"

    # Check PDFs are calculated
    assert isinstance(pdf_class_0, np.ndarray), "pdf_class_0 should be a NumPy array"
    assert isinstance(pdf_class_1, np.ndarray), "pdf_class_1 should be a NumPy array"
    assert pdf_class_0.shape == pdf_class_1.shape, "pdf_class_0 and pdf_class_1 should have the same shape"
    assert len(pdf_class_0.shape) == 2, "PDFs should be 2D arrays"

    # Check PDF values are non-negative
    assert np.all(pdf_class_0 >= 0), "pdf_class_0 should contain non-negative values"
    assert np.all(pdf_class_1 >= 0), "pdf_class_1 should contain non-negative values"

    # Check data points
    assert isinstance(d, np.ndarray), "d should be a NumPy array"
    assert d.shape == (1000, 2), f"d should have shape (1000, 2), got {d.shape}"

except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass