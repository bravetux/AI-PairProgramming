from collections import Counter
import string
import re

# 1. Palindrome Number
def is_palindrome(num):
    """
    Check if a given number is a palindrome.
    A palindrome number reads the same forward and backward.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(num) == str(num)[::-1]

# 2. Pangram Check
def is_pangram(sentence):
    """
    Check if a sentence is a pangram.
    A pangram contains every letter of the alphabet at least once.
    
    Args:
        sentence (str): The sentence to check.
    
    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

# 3. Anagram Check
def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams.
    Anagrams are words or phrases formed by rearranging the letters of another.
    
    Args:
        str1 (str): First string.
        str2 (str): Second string.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(str1) == sorted(str2)

# 4. Character Frequency
def char_frequency(s):
    """
    Count the frequency of each character in a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        dict: Dictionary with characters as keys and their frequencies as values.
    """
    return Counter(s)

# 5. Armstrong Number Check
def is_armstrong(num):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is equal to the sum of its own digits each raised to the power of the number of digits.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

# 6. Armstrong Numbers in Range
def armstrong_in_range(start, end):
    """
    Find all Armstrong numbers within a given range.
    
    Args:
        start (int): Start of the range.
        end (int): End of the range.
    
    Returns:
        list: List of Armstrong numbers in the range.
    """
    return [num for num in range(start, end + 1) if is_armstrong(num)]

# 7. Primes Using Sieve of Eratosthenes
def sieve(n):
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): Upper limit to generate primes.
    
    Returns:
        list: List of prime numbers up to n.
    """
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]

# 8. Optimized Prime Printing
def optimized_primes(n):
    """
    Wrapper function to generate primes using the optimized sieve method.
    
    Args:
        n (int): Upper limit to generate primes.
    
    Returns:
        list: List of prime numbers up to n.
    """
    return sieve(n)

# 9. Word Frequency
def word_frequency(sentence):
    """
    Count the frequency of each word in a sentence.
    
    Args:
        sentence (str): Input sentence.
    
    Returns:
        dict: Dictionary with words as keys and their frequencies as values.
    """
    words = sentence.lower().split()
    return Counter(words)

# 10. Reverse Each Word
def reverse_words(sentence):
    """
    Reverse each word in a sentence individually.
    
    Args:
        sentence (str): Input sentence.
    
    Returns:
        str: Sentence with each word reversed.
    """
    return ' '.join(word[::-1] for word in sentence.split())

# 11. Password Strength Check
def is_strong_password(password):
    """
    Check if a password is strong.
    A strong password must contain at least one uppercase letter, one lowercase letter,
    one digit, and one special character.
    
    Args:
        password (str): Password string.
    
    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    return (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and
            re.search(r'\W', password))

# 12. String to Integer (atoi)
def atoi(s):
    """
    Convert a string to an integer (similar to C's atoi).
    
    Args:
        s (str): Input string.
    
    Returns:
        int or None: Converted integer or None if conversion fails.
    """
    try:
        return int(s)
    except ValueError:
        return None

# 13. Decimal to Binary
def decimal_to_binary(n):
    """
    Convert a decimal number to binary representation.
    
    Args:
        n (int): Decimal number.
    
    Returns:
        str: Binary string without '0b' prefix.
    """
    return bin(n)[2:]

# 14. Decimal to Hexadecimal
def decimal_to_hex(n):
    """
    Convert a decimal number to hexadecimal representation.
    
    Args:
        n (int): Decimal number.
    
    Returns:
        str: Hexadecimal string without '0x' prefix.
    """
    return hex(n)[2:]

# Example usage
if __name__ == "__main__":
    print("Palindrome:", is_palindrome(121))
    print("Pangram:", is_pangram("The quick brown fox jumps over the lazy dog"))
    print("Anagrams:", are_anagrams("listen", "silent"))
    print("Character Frequency:", char_frequency("hello world"))
    print("Armstrong Check:", is_armstrong(153))
    print("Armstrong in Range:", armstrong_in_range(100, 999))
    print("Primes:", sieve(50))
    print("Optimized Primes:", optimized_primes(100))
    print("Word Frequency:", word_frequency("Hello world hello"))
    print("Reverse Words:", reverse_words("Hello world"))
    print("Strong Password:", is_strong_password("Passw0rd!"))
    print("Atoi:", atoi("123"))
    print("Binary:", decimal_to_binary(10))
    print("Hexadecimal:", decimal_to_hex(255))

