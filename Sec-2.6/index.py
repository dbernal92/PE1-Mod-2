# 2.6.1 The input() function
# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# 2.6.2 The input() function with an argument
# anything = input("Tell me anything...") Prompts user without print()
# print("Hmm...", anything, "...Really?")

# The results of input() is always a string

# 2.6.4 The input() function – prohibited operations
# Testing a TypeError message.

# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

# 2.6.5 Type casting (type conversions)
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Enter a number: 32
# 32.0 to the power of 2 is 1024.0

# 2.6.6 More about input() and type casting
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# Input first leg length: 3
# Input second leg length: 4
# Hypotenuse length is 5.0