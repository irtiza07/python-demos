import timeit

# String expressions
# print(timeit.timeit('[i for i in range(1000)]', number=10))
# print(timeit.timeit('[i for i in range(1000)]', number=1000))
# print(timeit.timeit('[i for i in range(1000)]', number=10_000))
# print(timeit.timeit('[i for i in range(1000)]', number=100_000))


# Measure function calls
# def loop_with_for():
#     print("For loop function..")
#     numbers = []
#     for i in range(1000_000):
#         numbers.append(i)
#     return numbers

# def loop_with_while():
#     print("While loop function..")
#     i = 0
#     numbers = []
#     while i < 1000_000:
#         numbers.append(i)
#         i += 1
#     return numbers

# print(timeit.timeit(loop_with_for, number=5))
# print(timeit.timeit(loop_with_while, number=5))