# task-1 **args and **kwargs

# for sum of numbers
def sum_of_numbers(*args):
    return sum(args)

print(sum_of_numbers(10, 20, 30, 40, 50))
print(sum_of_numbers(2.5, 3.7, 1.3))


# for string concatenation
def concat_strings(*args):
    return ''.join(args)

print(concat_strings("FUSE", " ", "Machines")) 

# total cost using keyword arguments
def calculate_total_cost(**kwargs):
    total_cost = 0
    for item, price in kwargs.items():
        total_cost += price
    return total_cost

print(calculate_total_cost(item1=10, item2=20, item3=30))


# student report using kwargs
def create_student_report(name, age, **kwargs):
    student_info = {
        "name": name,
        "age": age,
        "subjects": []
    }

    for subject, score in kwargs.items():
        student_info["subjects"].append({
            "subject": subject,
            "score": score
        })

    return student_info

print(create_student_report("Alice", 18, math=90, science=85, history=78))


