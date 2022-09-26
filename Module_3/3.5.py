"""Exercise 3.5: Write a test function for Exercise 3.4
Write a test function test_F_C that checks the computation of C(F(c)) and
F(C(f)), involving the C(F) and F(C) functions in Exercise 3.4.
Hint: Use a tolerance in the comparison. Let the test function follow the conven-
tions in the nose and pytest frameworks (see Sect. 3.3.3 for a first intro and Sect. H.9
for more overview).
"""

def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

def test_F_C():
    for i in range (0, 1000):        
        assert i - 0.001 < C(F(i)) < i + 0.001
        assert i - 0.001 < F(C(i)) < i + 0.001
test_F_C()