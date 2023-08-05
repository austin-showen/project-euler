# Largest Palindrome Product
# projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(n):
    # If n = 3, the loop will start at 999...
    # ...and end at 100. I separated these out for clarity.
    start = 10 ** n - 1
    end = 10 ** (n-1) - 1
    max_product = 0

    for i in range(start, end, -1):
        # This means we've already found the max product, so break early.
        if i * 1000 < max_product:
            break

        for j in range(start, end, -1):
            if i * j < max_product:
                break

            product = str(i * j)
            # Check if the product string is a palindrome.
            if product == product[::-1]:
                max_product = i * j

    return max_product


print(largest_palindrome_product(3))
