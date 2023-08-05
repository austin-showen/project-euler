# Smallest Multiple
# projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def evenly_divisible(start, end):
    num = end
    while True:
        divisible = True
        for divisor in range(start, end + 1):
            if num % divisor != 0:
                divisible = False
                num += end
                break
        if divisible == True:
            return num


print(evenly_divisible(1, 20))
