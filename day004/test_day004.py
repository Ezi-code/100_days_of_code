from day004 import get_number_type

def test_get_number_type():
    assert get_number_type(2) == True
    assert get_number_type(3) == False
    assert get_number_type(0) == False
    assert get_number_type(-1) == False
    assert get_number_type(-2) == False
