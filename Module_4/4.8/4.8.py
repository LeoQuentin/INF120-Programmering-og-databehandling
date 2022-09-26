"""Exercise 4.8: Try MSWord or LibreOffice to write a program
The purpose of this exercise is to tell you how hard it may be to write Python
programs in the standard programs that most people use for writing text.
a)
Type the following one-line program in either MSWord or LibreOffice:
print "Hello, World!"
Both Word and LibreOffice are so “smart” that they automatically edit “print”
to “Print” since a sentence should always start with a capital. This is just an
example that word processors are made for writing documents, not computer
programs.
b)
Save the program as a .docx (Word) or .odt (LibreOffice) file. Now try to run
this file as a Python program. What kind of error message do you get? Can you
explain why?
c) 
Save the program as a .txt file in Word or LibreOffice and run the file as 
a Python program. What happened now? Try to find out what the problem
is.
"""

# b) 
# The error message is:
# /usr/local/bin/python3: can't find '__main__' module in '/Users/leoquentin/Downloads/helloworldtest.docx'


# c)
with open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.8/helloworldtest.txt", "r") as f:
    helloworldtestContents = f.read()

exec(helloworldtestContents)