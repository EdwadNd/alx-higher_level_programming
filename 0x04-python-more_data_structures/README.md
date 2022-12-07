# 0x04. Python - More Data Structures: Set, Dictionary

###  0- Write a function that computes the square value of all integers of a matrix.
### 1 - Write a function that replaces all occurrences of an element by another in a new list.
### 2 - Write a function that adds all unique integers in a list (only once for each integer).
### 5:wqWrite a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any module
### 4 - Write a function that returns a set of all elements present in only one set.
### 5 - Write a function that returns the number of keys in a dictionary.

Prototype: def number_keys(a_dictionary):
You are not allowed to import any module
### 6 - Write a function that prints a dictionary by ordered keys.

Prototype: def print_sorted_dictionary(a_dictionary):
You can assume that all keys are strings
Keys should be sorted by alphabetic order
Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
Dictionary values can have any type
You are not allowed to import any module

### 7 - Write a function that replaces or adds key/value in a dictionary.

Prototype: def update_dictionary(a_dictionary, key, value):
key argument will be always a string
value argument will be any type
If a key exists in the dictionary, the value will be replaced
If a key doesn’t exist in the dictionary, it will be created
You are not allowed to import any module

### 8 - Write a function that deletes a key in a dictionary.

Prototype: def simple_delete(a_dictionary, key=""):
key argument will be always a string
If a key doesn’t exist, the dictionary won’t change
You are not allowed to import any module

### 9 - Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
### 10 - Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module
### 11 - Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified
You are not allowed to import any module
You have to use map
Your file should be max 3 lines

### 12 - Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0
