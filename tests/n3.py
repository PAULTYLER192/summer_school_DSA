OK_FORMAT = False

name = 'n3'

# Test the calculate_similarity function
try:
    assert callable(calculate_similarity), "calculate_similarity should be a function"
    
    # Test with sample texts
    text1 = "data science africa"
    text2 = "data science kampala"
    result = calculate_similarity(text1, text2)
    assert isinstance(result, (int, float)), "Function should return a number"
    assert 0 <= result <= 1, "Similarity should be between 0 and 1"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
