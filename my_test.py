import pytest;
import random;

def maketuple(input):
        return (input,input**2);


# Asserts that a tuple contains integers only
def test_maketuple1():
        res = maketuple(555);
        assert isinstance(res[0], int) == True;
        assert isinstance(res[1], int) == True;


# Asserts that second integer is really a power of two of the first one
def test_maketuple2():
        assert maketuple(42) == (42, 42**2);


def convertinttostring(input):
        return (input, str(input));

# Asserts we get a tuple containing an integer and a string corresponding to this integer
@pytest.mark.parametrize("input,expected", [(1, (1, '1')), (666, (666, '666'))])
def test_convertinttostring(input, expected):
        assert convertinttostring(input) == expected;




def makenegativefloat():
        return random.uniform(-1000, 0.00001);

# Asserts that a float is negative
def test_makenegativefloat():
        assert makenegativefloat() < 0;


def myeval(op: str, arg1: float, arg2: float) -> float:
        if not (isinstance(arg1, float) & isinstance(arg2, float)):
                raise TypeError("Second and third arguments must be floats!");
        return eval(str(arg1) + op + str(arg2));

# Asserts that the function throws right exceptions on non-valid arguments
def test_myeval1():
        try:
                assert myeval('?', 1.0, 333.333);
        except SyntaxError:
                pass

        try:
                assert myeval('+', '44a', 333.444);
        except TypeError:
                pass
