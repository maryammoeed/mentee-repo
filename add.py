def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Correct function call with argument
result = calculate_area(5)  # Example radius value

# Correct print statement with proper parentheses
print("The area is: " + str(result))  # Convert result to string for concatenation

# Safe division check to avoid division by zero
x = 10
y = 2  # Avoid division by zero
z = x / y
print("Result of division: " + str(z))  # Convert result to string for concatenation

# Correct variable usage (assuming 'a' should be 'result')
print(result)
