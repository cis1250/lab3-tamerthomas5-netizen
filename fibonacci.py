#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Fibonacci Sequence Generator

def get_positive_integer():
    while True:
        user_input = input("Enter the number of terms you want in the Fibonacci sequence: ")
        if user_input.isdigit():  # checks if input contains only digits
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a positive integer greater than 0.")
        else:
            print("Please enter a positive integer.")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # new line at the end

def main():
    terms = get_positive_integer()
    fibonacci(terms)

if __name__ == "__main__":
    main()
