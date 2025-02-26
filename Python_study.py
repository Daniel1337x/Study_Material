# Variable = A container that stores data values. (string, integer, float, boolean, list, tuple, dictionary, set)
#            A variable behaves as if it was the value it contains.
#            A variable is created the moment you first assign a value to it.


# Strings               age = "30" is technically a string.
first_name = "John"  # string
last_name = "Doe"  # string

# Integers
age = 30  # integer
quantity = 3 # integer          quantity = 3.5 is technically an integer.

print(f"You are {age} years old.")

# Floats
weight = 70
height = 1.75   # float
is_student = True  # boolean
food = "pizza"  # string



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