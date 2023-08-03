# task-6 exception handling

# divided by 0
def div(a,b):
    if b==0:
        raise ValueError("cannot divide by 0")
    return a/b

num1 = int(input("enter a"))
num2 = int(input("enter b"))
print(div(num1,num2))


# invalid integer
try:
    user_input = input("Enter an integer: ")
    integer_value = int(user_input)
    print("Integer value:", integer_value)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# both value error and division error
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = num1 / num2
    print("Result of division:", result)
except ValueError:
    print("Error: Please enter valid integers for both numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# invalid age
class InvalidAgeError(Exception):
    pass

def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            raise InvalidAgeError
        return age
    except ValueError:
        print("Error: Please enter a valid integer for age.")
        return get_age()
    except InvalidAgeError:
        print("Error: Invalid age. Age must be between 0 and 120.")
        return get_age()

user_age = get_age()
print("Your age:", user_age)
