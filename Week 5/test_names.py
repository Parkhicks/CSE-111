from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest
given_name="Parker"
family_name="Hicks"
def test_make_full_name():
    assert make_full_name("Parker","Hicks") == "Hicks; Parker"
    assert make_full_name("parker","Hicks") == "Hicks; parker"
    assert make_full_name("parker","hicks") == "hicks; parker"
    assert make_full_name("Parker","hicks") == "hicks; Parker"
    assert make_full_name("Bob","Smith") == "Smith; Bob"
    assert make_full_name("bob","Smith") == "Smith; bob"
    assert make_full_name("Bob","smith") == "smith; Bob"
    assert make_full_name("bob","smith") == "smith; bob"
    assert make_full_name("Amelia-Rose", "Stewart") == "Stewart; Amelia-Rose"


def test_extract_family_name():
    assert extract_family_name("Hicks; Parker") == "Hicks"
    assert extract_family_name("hicks; Parker") == "hicks"
    assert extract_family_name("Smith; Bob") == "Smith"
    assert extract_family_name("smith; Bob") == "smith"
    assert extract_family_name("Stewart; Amelia-Rose") == "Stewart"


def test_extract_given_name():
    assert extract_given_name("Hicks; Parker") == "Parker"
    assert extract_given_name("Hicks; parker") == "parker"
    assert extract_given_name("Smith; bob") == "bob"
    assert extract_given_name("Smith; Bob") == "Bob"
    assert extract_given_name("Stewart; Amelia-Rose") == "Amelia-Rose"






# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])