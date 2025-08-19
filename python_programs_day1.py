from collections import Counter
import string
import re

# 1. Palindrome Number
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 2. Pangram Check
def is_pangram(sentence):
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

# 3. Anagram Check
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# 4. Character Frequency
def char_frequency(s):
    return Counter(s)

# 5. Armstrong Number Check
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

# 6. Armstrong Numbers in Range
def armstrong_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

# 7. Primes Using Sieve of Eratosthenes
def sieve(n):
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
    return sieve(n)

# 9. Word Frequency
def word_frequency(sentence):
    words = sentence.lower().split()
    return Counter(words)

# 10. Reverse Each Word
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# 11. Password Strength Check
def is_strong_password(password):
    return (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and
            re.search(r'\W', password))

# 12. String to Integer (atoi)
def atoi(s):
    try:
        return int(s)
    except ValueError:
        return None

# 13. Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]

# 14. Decimal to Hexadecimal
def decimal_to_hex(n):
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

