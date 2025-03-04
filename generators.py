from datetime import datetime, timedelta

# Generator that generates squares of numbers up to N
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# Generator for even numbers up to n
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Generator for numbers divisible by 3 and 4 up to n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Generator yielding squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Generator counting down from n to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

