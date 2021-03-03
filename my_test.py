import pytest;
import random;

def maketuple():
        return (1,2);

# Makes sure that a tuple contains integers only
def test_maketuple():
        res = maketuple();
        assert isinstance(res[0], int) == True;
        assert isinstance(res[1], int) == True;



def makenegativefloat():
        return random.uniform(-1000, 0.00001);

# Makes sure that a float is negative
def test_makenegativefloat():
        assert makenegativefloat() < 0;



def convertinttostring(input):
        return (input, str(input));

# Makes sure we get a tuple containing an integer and a string representing this integer
@pytest.mark.parametrize("input,expected", [(1, (1, '1')), (666, (666, '666'))])
def test_convertinttostring(input, expected):
        assert convertinttostring(input) == expected;

