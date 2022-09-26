"""
Exercise 3.6: Given a test function, write the function
Here is a test function:
def test_double():
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15
    assert double([1, 2]) == [1, 2, 1, 2]
    assert double((1, 2)) == (1, 2, 1, 2)
    assert double(3+4j) == 6+8 j
    assert double(’hello’) == ’hellohello’
    Write the associated function to be tested (double) and run test_double.
"""
def double(x):
    return x*2

def test_double():
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15
    assert double([1, 2]) == [1, 2, 1, 2]
    assert double((1, 2)) == (1, 2, 1, 2)
    assert double(3+4j) == 6+8j
    assert double("hello") == "hellohello"
    
test_double()
