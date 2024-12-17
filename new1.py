# Function to calculate the factorial of a number
def calculate_factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Function to read a number from a file and calculate its factorial
def read_number_and_calculate_factorial(file_path):
    try:
        # Read number from the file
        with open(file_path, 'r') as file:
            number = int(file.read().strip())  # Read the number and strip any extra spaces/newlines
            print(f"Calculating factorial of {number}...")
            result = calculate_factorial(number)
            print(f"The factorial of {number} is {result}")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to execute the code
def main():
    file_path = "number.txt"  # Path to the file containing a number
    read_number_and_calculate_factorial(file_path)

if __name__ == "__main__":
    main()
