# task-5 comprehension


# list comprehension

# more than 5 characters
original_list = ["apple", "banana", "orange", "cherry", "grape", "kiwi", "watermelon"]

result_list = [word for word in original_list if len(word) > 5]

print(result_list)

# product of items between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

product_list = [list1[i] * list2[i] for i in range(min(len(list1), len(list2)))]

print(product_list)


# dict comprehension

# key from 1 list, value from other list
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

my_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

print(my_dict)

# key students and marks values with marks greater than 80
scores_dict = {
    'riaz': 85,
    'puja': 70,
    'bipin': 90,
    'prateek': 78,
    'gunjan': 95,
    'rojesh': 82
}

# New dictionary with students who scored more than 80
high_scores_dict = {name: score for name, score in scores_dict.items() if score > 80}

print(high_scores_dict)


# set comprehension

# set containing only unique even numbers
numbers_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]

unique_even_set = {num for num in numbers_list if num % 2 == 0}

print(unique_even_set)

# set containing unique characters
words_list = ["apple", "banana", "orange", "cherry"]

unique_characters_set = {char for word in words_list for char in word}

print(unique_characters_set)
 


