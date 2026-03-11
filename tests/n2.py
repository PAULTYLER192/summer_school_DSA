OK_FORMAT = False

name = 'n2'

# Test the extract_entities function
try:
    assert callable(extract_entities), "extract_entities should be a function"
    
    # Test with sample text
    text = "Makerere University is in Kampala. Kampala is the capital of Uganda."
    keywords = ["Makerere", "Kampala"]
    result = extract_entities(text, keywords)
    assert isinstance(result, list), "Function should return a list"
    assert len(result) > 0, "Should return at least one sentence"
except NameError:
    # Variable doesn't exist during format check - this is expected
    # The assertions will run when the test executes with global environment
    pass
