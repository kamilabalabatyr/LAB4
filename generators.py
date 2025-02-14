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

if __name__ == "__main__":
    N = 10
    print("Squares up to N:", list(square_generator(N)))
    
    n = int(input("Enter n for even numbers: "))
    print("Even numbers:", ", ".join(map(str, even_numbers(n))))
    
    n = int(input("Enter n for numbers divisible by 3 and 4: "))
    print("Divisible by 3 and 4:", list(divisible_by_3_and_4(n)))
    
    a, b = 1, 5
    print("Squares from a to b:")
    for num in squares(a, b):
        print(num)
    
    n = int(input("Enter n for countdown: "))
    print("Countdown:", list(countdown(n)))
