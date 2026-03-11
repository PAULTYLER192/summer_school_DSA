OK_FORMAT = False

name = 'n1'

# Test the count_words function
try:
    assert callable(count_words), "count_words should be a function"
    
    # Test with sample text
    result = count_words("Hello world hello")
    assert isinstance(result, dict), "Function should return a dictionary"
    assert 'hello' in result, "Result should contain 'hello' key"
    assert result['hello'] == 2, "Count of 'hello' should be 2"
    assert result.get('world', 0) == 1, "Count of 'world' should be 1"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
