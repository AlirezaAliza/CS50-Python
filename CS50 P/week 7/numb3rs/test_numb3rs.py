from numb3rs import validate


def test_ip():
    assert validate
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("192.168.1.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.2") == False
    assert validate("192.168.1.256") == False
    assert validate("alireza") == False
    assert validate("192.168.1.255.1") == False
    assert validate("300.300.300.300") == False
    assert validate("300.300.300.300.300") == False
    assert validate("ali.ali.ali.ali") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
