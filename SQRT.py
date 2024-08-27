#Emre 2024

#The code calculates the square root of a number using the Newton-Raphson method for 
# non-negative inputs and the complex square root function for negative inputs. 
# For non-negative numbers, it employs a recursive function to iteratively apply 
# the Newton-Raphson update formula until the result converges within a specified tolerance. 
# The function determines which method to use based on whether the input is negative or 
# non-negative, and the program prompts the user for input, computes the square root.




import cmath

# Function to calculate the average of y and x/y, used for finding the square root
def sqrt (y, x):
    return ((y+(x/y))/2)


# Function to find the fixed point of a function f, starting from 'start' and using 'x' as a parameter.
# It stops iterating when the change between iterations is smaller than 'tolerance'.
def fixed_Point(f, start, x, tolerance=0.000001):

    # Helper function to determine if the difference between two values is within the tolerance
    def close_enuf(u, v):
        return abs(u - v) < tolerance

    # Recursive function to iteratively apply the function f until the result is stable    
    def iter(old, new):
        if close_enuf(old, new):
            return new
        else:
            return iter(new, f(new, x))
    # Start the iteration with 'start' and apply function f to find the fixed point    
    return iter(start, f(start, x))


# Function to compute the square root of x
# Uses cmath.sqrt for negative numbers and fixed-point iteration for non-negative numbers
def safe_sqrt(x):
    if x < 0:
        return cmath.sqrt(x)    # Uses cmath.sqrt for negative numbers (returns a complex number)
    elif x == 0:
        return 0    # Square root of 0 is 0
    else:
        initial_guess = x / 2   # Start with an initial guess
        return fixed_Point(sqrt, initial_guess, x)  # Find the square root using fixed-point iteration

# Prompt the user to enter a number
print()
x = int(input("Please enter the number you want to find the square root of: "))

# Compute the square root
result = safe_sqrt(x)

# Print the result
print()
print(f"The square root of {x} is approximately {result}")
print()
