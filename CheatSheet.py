# This file contains information for print function, variable definition and declaration
# Also contains data type conversion
# Also contains string formatting and string functions

# Print the line
print("This is python learning")

# define the various data type
# INT - define int variable
val = 10
print(val)

# INT - update value of val variable
val = 20
print(val)

# FLOAT - define float variable
float_val = 10.03
print(float_val)
# or
float_val = float(10.04)
print (float_val)

# BOOL - STRING define boolean and string variables
name = 'minal'
print(name)

is_female = True
print(is_female)

# INPUT - user input
name = input("Enter your name: ")
print(name)

# type conversion in python
birth_year = input("Enter your birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(age)

# STRING - define string
str_val = 'this is python learning'
print(str_val)
str_val = "this is python learning"
print(str_val)

# define formatted string
email = '''
Hi Sir,

This is sample email. Please revert me back.

Thanks
Minal 
'''
print(email)

# return the part of string
str_val = 'this is python learning'
print(str_val[0:3])
print(str_val[:])
print(str_val[1:-1]) # this will return start from 1 to last character -1

# dynamic build the string
name = "Minal"
course = "Python"
msg = f'This is {name}. I am enrolled in {course}'
print(msg)

# replace the string
course = "Python for Beginners"
print(course.replace("P","J"))
print(course.find("Beg")) # find method returns the index

# in operator
print("py" in course)

# different string methods
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('for'))
print(course.replace('for', 'FOR'))












