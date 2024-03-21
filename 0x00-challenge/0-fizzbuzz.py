#!/usr/bin/python3
""" FizzBuzz

This script implements the FizzBuzz problem, which prints numbers from 1 to n separated by a space.

- For multiples of three, it prints "Fizz" instead of the number.
- For multiples of five, it prints "Buzz".
- For numbers that are multiples of both three and five, it prints "FizzBuzz".
"""

import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    Parameters:
        n (int): The upper limit for printing numbers.

    Returns:
        None: Prints the FizzBuzz sequence.
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
