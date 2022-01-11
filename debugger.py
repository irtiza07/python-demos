import ipdb

def make_square(a):
    return a * a

# see values of attributes
# n = next linew
# c = continue till hitting breakpoint
# b <line_no>  = set breakpoints
ipdb.set_trace()
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    result = make_square(number)
    squares.append(number)

print(squares)