# Largest Prime Factor
# projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    while n > 1:
        factor = 2
        while n % factor != 0:
            factor += 1
        n /= factor
    return factor


print(largest_prime_factor(600851475143))  # 6857
