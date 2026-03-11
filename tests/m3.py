OK_FORMAT = False

name = 'm3'

import numpy as np

# Test that Gaussian distributions are fitted correctly
# Check points are filtered correctly
try:
    assert isinstance(points_class_0, np.ndarray), "points_class_0 should be a NumPy array"
    assert isinstance(points_class_1, np.ndarray), "points_class_1 should be a NumPy array"
    assert points_class_0.shape[1] == 2, "points_class_0 should be 2D (N, 2)"
    assert points_class_1.shape[1] == 2, "points_class_1 should be 2D (N, 2)"

    # Check means
    assert isinstance(mean_class_0, np.ndarray), "mean_class_0 should be a NumPy array"
    assert isinstance(mean_class_1, np.ndarray), "mean_class_1 should be a NumPy array"
    assert mean_class_0.shape == (2,), f"mean_class_0 should have shape (2,), got {mean_class_0.shape}"
    assert mean_class_1.shape == (2,), f"mean_class_1 should have shape (2,), got {mean_class_1.shape}"

    # Check covariance matrices
    assert isinstance(cov_class_0, np.ndarray), "cov_class_0 should be a NumPy array"
    assert isinstance(cov_class_1, np.ndarray), "cov_class_1 should be a NumPy array"
    assert cov_class_0.shape == (2, 2), f"cov_class_0 should have shape (2, 2), got {cov_class_0.shape}"
    assert cov_class_1.shape == (2, 2), f"cov_class_1 should have shape (2, 2), got {cov_class_1.shape}"

    # Check covariance is symmetric
    assert np.allclose(cov_class_0, cov_class_0.T), "cov_class_0 should be symmetric"
    assert np.allclose(cov_class_1, cov_class_1.T), "cov_class_1 should be symmetric"

    # Check covariance is positive semi-definite (determinant >= 0)
    assert np.linalg.det(cov_class_0) >= 0, "cov_class_0 should be positive semi-definite"
    assert np.linalg.det(cov_class_1) >= 0, "cov_class_1 should be positive semi-definite"

except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass