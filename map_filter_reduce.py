# task2 Map, Filter and Reduce

# convert to uppercase using map
def convert_to_uppercase(input_list):
    return list(map(str.upper, input_list))

input_strings = ["hello", "FuSemachine's", "changemakers"]
result = convert_to_uppercase(input_strings)
print(result)


# filtering prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime_numbers(input_list):
    return list(filter(is_prime, input_list))

input_numbers = [17, 20, 23, 29, 32, 37, 41]
result = filter_prime_numbers(input_numbers)
print(result)

# factorial using reduce

from functools import reduce

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(calculate_factorial(0))
print(calculate_factorial(5))
