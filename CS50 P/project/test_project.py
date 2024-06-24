from project import number_1, number_2, op

def test_check_for_number_1 ():

    assert number_1("ali") == False
    assert number_1 ("123") == True
def test_check_for_op ():

    assert op ("plus") == False
    assert op ("+") == True
def test_check_for_number_2 ():

    assert number_2 ("Harvard") == False
    assert number_2 ("5462") == True
