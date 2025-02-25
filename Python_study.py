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

