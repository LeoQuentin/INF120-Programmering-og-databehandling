"""Exercise 4.6: Read input from the keyboard
Make a program that asks for input from the user, applies eval to this input, and
prints out the type of the resulting object and its value. Test the program by pro-
viding five types of input: an integer, a real number, a complex number, a list, and
a tuple.
"""
def userInputManual():
    try:
        user_input = eval(input("Please provide an input: "))
        return(user_input)
    except:
        print("Please provide a valid input (either an integer, a real number, a complex number, a list, or a tuple)")
        quit()


def print_type_and_value(a, b):
    try:
        resultingNumber = (a + b)
        return resultingNumber, type(resultingNumber)
    except:
        print("Please provide a valid input (either an integer, a real number, a complex number, a list, or a tuple)")
        quit()

resulting_number, type_of_number = print_type_and_value(userInputManual(), userInputManual())
print(f"The resulting value is {resulting_number} and the type is {type_of_number}")


def test_function():
    allowedVariance = 1E-6
    assert print_type_and_value(1, 2) == (3, int)
    assert 3 - allowedVariance < print_type_and_value(1.0, 2.0)[0] < 3.0 + allowedVariance
    assert print_type_and_value(1j, 2j) == (3j, complex)
    assert print_type_and_value([1, 2, 3], [4, 5, 6]) == ([1, 2, 3, 4, 5, 6], list)
    assert print_type_and_value((1, 2, 3), (4, 5, 6)) == ((1, 2, 3, 4, 5, 6), tuple)

test_function()