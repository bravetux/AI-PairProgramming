# Day 2 Python Programs with Detailed Comments

from typing import List

# 1. Print all the factors of a given number
def print_factors(n: int) -> List[int]:
    """
    Returns a list of all factors of the given number n.
    A factor is a number that divides n without leaving a remainder.
    """
    return [i for i in range(1, n + 1) if n % i == 0]

# 2. Print if the two given strings are equal or unequal
def compare_strings(s1: str, s2: str) -> str:
    """
    Compares two strings and returns whether they are equal or unequal.
    """
    return "Equal" if s1 == s2 else "Unequal"

# 3. Print the frequency of the given character in the given string
def char_frequency(s: str, ch: str) -> int:
    """
    Returns the number of times character ch appears in string s.
    """
    return s.count(ch)

# 4. Print the number of vowels in the given string
def count_vowels(s: str) -> int:
    """
    Counts and returns the number of vowels in the string s.
    Vowels considered: a, e, i, o, u (case-insensitive).
    """
    return sum(1 for c in s.lower() if c in 'aeiou')

# 5. Print all the numbers divisible by a given number in a range
def divisible_in_range(start: int, end: int, divisor: int) -> List[int]:
    """
    Returns a list of numbers between start and end (inclusive) that are divisible by divisor.
    """
    return [i for i in range(start, end + 1) if i % divisor == 0]

# 6. Find the factorial of a number with recursion
def factorial_recursive(n: int) -> int:
    """
    Recursively calculates the factorial of n.
    Base case: factorial(0) = 1
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# 6. Find the factorial of a number without recursion
def factorial_iterative(n: int) -> int:
    """
    Iteratively calculates the factorial of n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 7. Display the Fibonacci series with recursion
def fibonacci_recursive(n: int) -> List[int]:
    """
    Returns the first n Fibonacci numbers using recursion.
    Note: This is not efficient for large n due to repeated calculations.
    """
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)
    return [fib(i) for i in range(n)]

# 7. Display the Fibonacci series without recursion
def fibonacci_iterative(n: int) -> List[int]:
    """
    Returns the first n Fibonacci numbers using iteration.
    """
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# 8. Print “Welcome” if your name is present in the list and “See you next time” if not
def greet_user(name: str, name_list: List[str]) -> str:
    """
    Checks if name is in name_list and returns a greeting accordingly.
    """
    return "Welcome" if name in name_list else "See you next time"

# 9. Find if the given number is a prime
def is_prime(n: int) -> bool:
    """
    Checks if n is a prime number.
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 10. Print the list of prime numbers in the given range
def primes_in_range(start: int, end: int) -> List[int]:
    """
    Returns a list of prime numbers between start and end (inclusive).
    """
    return [i for i in range(start, end + 1) if is_prime(i)]

# 11. Find if the given number is a perfect number
def is_perfect(n: int) -> bool:
    """
    Checks if n is a perfect number.
    A perfect number is equal to the sum of its proper divisors (excluding itself).
    """
    return sum(i for i in range(1, n) if n % i == 0) == n

# 12. Print the list of perfect numbers in the given range
def perfect_numbers_in_range(start: int, end: int) -> List[int]:
    """
    Returns a list of perfect numbers between start and end (inclusive).
    """
    return [i for i in range(start, end + 1) if is_perfect(i)]

# Example usage
if __name__ == "__main__":
    print("Factors of 12:", print_factors(12))
    print("Compare strings:", compare_strings("hello", "hello"))
    print("Character frequency:", char_frequency("banana", "a"))
    print("Vowel count:", count_vowels("education"))
    print("Divisible by 3 in range 1-20:", divisible_in_range(1, 20, 3))
    print("Factorial (recursive) of 5:", factorial_recursive(5))
    print("Factorial (iterative) of 5:", factorial_iterative(5))
    print("Fibonacci (recursive) 5 terms:", fibonacci_recursive(5))
    print("Fibonacci (iterative) 5 terms:", fibonacci_iterative(5))
    print("Greet user:", greet_user("Alice", ["Bob", "Alice", "Charlie"]))
    print("Is 17 prime?:", is_prime(17))
    print("Primes in range 10-30:", primes_in_range(10, 30))
    print("Is 28 perfect?:", is_perfect(28))
    print("Perfect numbers in range 1-1000:", perfect_numbers_in_range(1, 1000))

