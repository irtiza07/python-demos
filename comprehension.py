numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Simple list comprehension 
# squares = [i*i for i in numbers]
# print(squares)

# Conditional list comprehension
# squares_except_2 = [i*i for i in numbers if i != 2]

# Function + List comprehension
# def add_one(number):
#     return number + 1
# increment_1 = [add_one(i) for i in numbers]
# print(increment_1)

# Set comprehension same thing! Just removes duplicates!
# word = "aeiou aeiou aeiou"
# vowels_present_list = [ letter for letter in word if letter in ['a', 'e', 'i', 'o', 'u']]
# vowels_present_set = { letter for letter in word if letter in ['a', 'e', 'i', 'o', 'u']}
# print(vowels_present_list)
# print(vowels_present_set)

# Create dictionary with comprehensions
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares_dictionary = {i: i*i for i in numbers}
# print(squares_dictionary)

# Dictionary comprehension
student_scores = {
    'Bob': 100,
    'Alice': 50,
    'Max': 10
}
statements = [f"{name} received {score}" for name, score in student_scores.items()]
print(statements)
