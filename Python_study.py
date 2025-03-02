
import math
# Variable = A container that stores data values. (string, integer, float, boolean, list, tuple, dictionary, set)
#            A variable behaves as if it was the value it contains.
#            A variable is created the moment you first assign a value to it.


# Strings               age = "30" is technically a string.
first_name = "John"  # string
last_name = "Doe"  # string

# Integers              # whole numbers if age = "30" is technically a string.
age = 30  # integer
quantity = 3 # integer          quantity = 3.5 is technically an integer.

print(f"You are {age} years old.")

# Floats               # decimal numbers
weight = 70.99
height = 1.75   # float
is_student = True  # boolean
food = "pizza"  # string

price = 10.99

print(f"The price is ${price}.")

# Booleans             # true or false
is_student = True  # boolean
is_adult = False  # boolean

# Lists                # ordered collection of items enclosed in square brackets

# Typecasting = The process of converting a variable from one data type to another.
#               str() = string, int() = integer, float() = float, bool() = boolean

name = "John Connor" # string
age = 24 # integer
gpa = 3.2   # float
is_student = True # boolean

# gpa to interger
gpa = int(gpa)

print(gpa) # 3 (not 3.2) 0.2 is truncated!

# age to float
age = float(age)

print(age)  # 24.0

# age to string
age = str(age)

print(age)  # "24"

# name to boolean
name = bool(name)

print(name)  # True

# input()    = A function that prompts the user to enter data.
#              Returns the entered data as a string.

name = input("What is your name? ")  # "John Connor"
age = int(input("How old are you? "))  # "24"   The int() function converts the string to an integer.
# or
age = int(age)
age = age + 1

print(f "Hello, {name}!")
print("Happy Birthday!")
print(f"You are {age} years old.")

### EXERCISES ###
# Exercise 1 Rectangle Area Calc

lenght = input("Enter the lenght:")
width = input("Enter the width:")

area = int(lenght) * int(width) # Typecasting the string to an integer # * is asteric (multiplier)

print(f"The area is: {area}cm")

# Exercise 2 Shopping Cart Program

item = input("Enter the item you want to add to the cart: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total = price * quantity

print(f"Total price of {item} is: {total}")

#### Arithmetic Operators ####
# + = addition
# - = subtraction
# * = multiplication
# / = division
# % = modulus
# ** = exponentiation
# // = floor division

friends = 0
#friends = friends + 1
#friends += 1  # augmented assignment operator

print(friends)  # 1



x = 3.14
y = -4
z = 5

result = round(x)   # round() function rounds a number to the nearest integer
print(result)  # 3

result = abs(y)  # abs() function returns the absolute value of a number
print(result)  # 4

result = pow(4, 3)  # pow() function returns the power of a number
print(result)  # 64

max(x, y, z)  # max() function returns the largest of the given arguments)
result = max(x, y, z)
print(result)  # 5
#or
max(x, y, z)
result = max(x, y, z)       # max() function returns the largest of the given arguments)
result = min(x, y, z)
print(result)  # -4         # min() function returns the smallest of the given arguments)
print(result)  # 5


## added import math module to use math functions

print(math.pi)  # 3.141592653589793 using math module
print(math.e)  # 2.718281828459045 using math module, exponential constant


# square root module    
x = 9
result = math.sqrt(x)  # sqrt() function returns the square root of x
print(result)  # 3.0

### math exercises ###
# Exercise 1: Calculate the area of a circle

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference}")   # result is 31.415926535897
or 
print(f"The area of the circle is: {round(circumference)}")     # result is 31 (rounded)
or
print(f"The area of the circle is: {round(circumference, 2)}cm")  # result is 31.42 (rounded to 2 decimal places)


# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")       # indentation is important in Python ( space at the start of the line)         
elif  age < 0:
    print("You havent been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You must be 18 years old to sign up!")

response = input("Would you like to sign up? (yes/no): ")

if response == "yes":           # = assignemnt operator, == comparison operator
    print("Signing up...")
else:
    print("Goodbye!")


name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")  # indentation error
else:
    print(f"Hello, {name}!")


## Booleans in if statements ##
online = True
if online:
    print("The user is online.")
else:
    print("The user is offline.")


# Python calculator

operator = input("Enter the operator (+, -, *, /): ")
num1 = (input("Enter the first number: "))          # input() function returns a string  # num1 = 10 is an integer
num2 = float(input("Enter the second number: "))    # num2 = 5.5 is a float ! we want to convert it to float
print (num1 + num2)

if operator == "+":
    result = num1 + num2
    print(f"Result: {round(result)}")               # round() function rounds a number to the nearest integer
elif operator == "-":
    result = num1 - num2
    print(f"Result: {round(result, 3)}")            # round() function rounds a number to 3 decimal places
elif operator == "*":
    result = num1 * num2
    print(f"Result: {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Result: {round(result, 3)}")
else:
    print(f"Invalid operator: {operator}")

# Python weight converter ### Exercise ###

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (L)bs or (K)g: ")
if unit.upper() == "L":                             # .upper() function converts the string to uppercase
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")        # round() function rounds a number to 1 decimal places
elif unit.upper() == "K":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")        # round() function rounds a number to 1 decimal places
else:
    print(f"{unit} was not valid.")



# print f-string examples - all strings inside curly braces are evaluated as expressions
#expression = a combination of values, variables, and operators that evaluate to a single value
#expression = 1 + 2

print(f"Hello {first_name}")                            # f means format
print(f"You like {food}")
print(f"Your age is {age}")

full_name = f"{first_name} {last_name}"  # f-string formatting
greeting = "Hello, {full_name}!"   # f-string formatting


print(f"Hello, {full_name}!")

# Data Types
# 1. Text Type: str
# 2. Numeric Types: int, float, complex
# 3. Sequence Types: list, tuple, range
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview
# 7. Expression: expression is a combination of values, variables, and operators that evaluate to a single value.
# 8. Variable: A container that stores data values. (string, integer, float, boolean, list, tuple, dictionary, set)

# An expression is a combination of operators and operands that is interpreted to produce some other value. 
# In any programming language, an expression is evaluated as per the precedence of its operators. 
# So that if there is more than one operator in an expression, their precedence decides which operation will be performed first. 
# We have many different types of expressions in Python.

# 1. Constant Expressions: These are the expressions that have constant values only.
# Constant Expressions 
x = 15 + 1.3
  
print(x)

 

# 2. Arithmetic Expressions: An arithmetic expression is a combination of numeric values, operators, and sometimes parenthesis. 
# The result of this type of expression is also a numeric value. The operators used in these expressions are arithmetic operators like addition, subtraction, etc.


# Arithmetic Expressions 
x = 40
y = 12
  
add = x + y 
sub = x - y 
pro = x * y 
div = x / y 
  
print(add) 
print(sub) 
print(pro) 
print(div)


### Print examples ###



# Quick summary.

    print(f“hello, {name}”)
# f-strings are stylish, modern, extremely fast, powerful and have absolutely no relation to the print function. You can do result = f“hello, {name}”. Between braces you can put any expression, function calls, list comprehension, etc.


    print(“hello,” , name)
# Slow. Relies on the print statement for "kind of" concatenating the output. Always adds a space between arguments.


    print(“hello,” + name)
# String concatenation. Very slow. name must be a string. Not related to the print statement.


# Syntactic sugar. Doesn't really matter. Use whatever you like. The f-string is the most modern and powerful way to format strings in Python. The other two are just there for historical reasons.

print(f"{one}{two}{three}{four}")

versus

print("{}{}{}{}".format(
  one,
  two,
  three,
  four
))

### formating string literals examples ###
 
>>> name = "Fred"
>>> f"He said his name is {name}."
"He said his name is Fred."

>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is Fred."

>>> f"He said his name is {repr(name)}." # repr() is equivalent to !r
"He said his name is Fred."

>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}" # nested fields
result: 12.35

>>> today = datetime(year=2023, month=1, day=27)
>>> f"{today:%B %d, %Y}" # using date format specifier
January 27, 2023

>>> number = 1024
>>> f"{number:#0x}" # using integer format specifier
0x400