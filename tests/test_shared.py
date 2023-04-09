import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_assertion():
    assert 1 == 1
   

@pytest.mark.xfail
def test_failing():
    assert 1 == 2
    
@pytest.mark.skip(reason = "Because I said so")
def test_skip():
    assert "Green Eggs and Ham" == "Sam I am"
    
@pytest.mark.skipif(sys.platform == "windows", reason="This does not work on my platform")
def test_onlyplatform():
    print(sys.platform)
    assert "I hope I did this right" == "Probably not..."
