"""Exercise 4.15: Write a function given its test function
A common software development technique in the IT industry is to write the test
function before writing the function itself.
a) We want to write a function halve(x) that returns the half of its argument x.
The test function is
def test_halve():
    assert halve(5.0) == 2.5    # Real number division
    assert halve(5) == 2        # Integer division
Write the associated function halve. Call test_halve (or run pytest or nose)
to verify that halve works.
...
"""
# a)
def test_halve():
    assert halve(5.0) == 2.5
    assert halve(5) == 2

def halve(x):
    if type(x) == int:
        return int(x/2)
    elif type(x) == float:
        return x/2
    else:
        raise TypeError("Please provide an integer or a float")
test_halve()

# b) 
def test_add():
    # Test integers
    assert add(1, 2) == 3
    # Test floating-point numbers with rounding error
    tol = 1E-14
    a = 0.1; b = 0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol
    # Test lists
    assert add([1,4], [4,7]) == [1,4,4,7]
    # Test strings
    assert add("Hello, ", "World!") == "Hello, World!"

def add(a, b):
    return(a+b)
test_add()


# c)
def test_equal():
    assert equal("abc", "abc") == ( True, "abc")
    assert equal("abc", "aBc") == ( False, "ab|Bc")
    assert equal("abc", "aBcd") == ( False, "ab|Bc*|d")
    assert equal("Hello, World!", "hello world") == (False, "H|hello,|  |wW|oo|rr|ll|dd|*!|*")

def equal(a, b):
    if a == b:
        return (True, b)
    else:
        outputValue = []
        aLetters = ([*a])
        bLetters = ([*b])
        for i in range(0,(max(len(aLetters),len(bLetters)))):
            if i <= len(aLetters)-1 and i <= len(bLetters)-1:
                if aLetters[i] == bLetters[i]:
                    outputValue.append(aLetters[i])
                elif aLetters[i] != bLetters[i]:
                    outputValue.append(f"{aLetters[i]}|{bLetters[i]}")
            elif i > (len(aLetters)-1):
                outputValue.append(f"*|{bLetters[i]}")
            elif i > (len(bLetters)-1):
                outputValue.append(f"{aLetters[i]}|*")
        return (False, "".join(outputValue))
                            
test_equal()

# c) 