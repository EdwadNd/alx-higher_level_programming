### Python - Test-driven development

## Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
##  Write a function that divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
	matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
	Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
	div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
	div can't be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
	All elements of the matrix should be divided by div, rounded to 2 decimal places
	Returns a new matrix
	You are not allowed to import any module
## Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

	Prototype: def text_indentation(text):
	    text must be a string, otherwise raise a TypeError exception with the message text must be a string
	    There should be no space at the beginning or at the end of each printed line
	    You are not allowed to import any module

