import math
import json
import logging

def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n < 0:
        logging.error("Factorial is not defined for negative numbers")
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number."""
    if n <= 0:
        logging.warning(f"Fibonacci function received an invalid value {n}.")
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(number: int) -> bool:
    """Checks if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def sort_dict(dictionary: dict) -> dict:
    """Sorts a dictionary by its keys."""
    try:
        return dict(sorted(dictionary.items()))
    except TypeError as e:
        logging.error(f"Failed to sort dictionary: {e}")
        raise

def calculate_area(radius: float) -> float:
    """Calculates the area of a circle."""
    if radius <= 0:
        logging.error("Invalid radius value. Radius must be greater than zero.")
        raise ValueError("Radius must be greater than zero")
    return math.pi * radius ** 2

def process_json_data(json_data: str) -> dict:
    """Parses a JSON string and returns a Python dictionary."""
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data: {e}")
        raise

def main():
    # Test the functions
    try:
        # Testing factorial function with negative number
        print(factorial(-1))  # This will raise an error
        
        # Testing fibonacci function with invalid value
        print(fibonacci(-5))  # This will print a warning
        
        # Testing prime number check
        print(is_prime(17))  # True
        
        # Testing sorting function
        unsorted_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
        print(sort_dict(unsorted_dict))  # {'apple': 2, 'banana': 3, 'cherry': 1}
        
        # Testing area calculation
        print(calculate_area(-5))  # This will raise an error
        
        # Testing JSON processing
        json_data = '{"name": "Alice", "age": 25}'
        print(process_json_data(json_data))  # {'name': 'Alice', 'age': 25}
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
