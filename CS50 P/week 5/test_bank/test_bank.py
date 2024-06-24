from bank import value


def test_value_casesensitivity():
    assert value("hello") == 0
    assert value("HEllo") == 0



def test_value_firstletter():
    assert value("how you doing") == 20
    assert value("hoo hoo hoo") == 20



def test_value_failure():
    assert value("what does the fox say ?") == 100
    assert value("Aref") == 100
