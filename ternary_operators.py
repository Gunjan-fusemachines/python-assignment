# task-3 ternary operators

# check_even
def check_odd_even(number):
    return "Even" if number % 2 == 0 else "Odd"

print(check_odd_even(5)) 
print(check_odd_even(10)) 

# check leap year
def check_leap_year(year):
    is_leap = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"
    return is_leap

print(check_leap_year(1900))
print(check_leap_year(2024))

# find bigger number
def find_bigger_number(a, b, c):
    result = "Equal" if a == b == c else (a if a >= b and a >= c else (b if b >= c else c))
    return result

print(find_bigger_number(100, 50, 75))
print(find_bigger_number(8, 8, 8))
print(find_bigger_number(-5, -10, -3))