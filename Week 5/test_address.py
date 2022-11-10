from address import extract_city, extract_state,extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("163 E 2nd S, Rexburg, ID 83440") == "Rexburg"

def test_extract_state():
    assert extract_state("163 E 2nd S, Rexburg, ID 83440") == "ID"
    
def test_extract_zipcode():
    assert extract_zipcode("163 E 2nd S, Rexburg, ID 83440") == "83440"




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])