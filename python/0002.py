# Even Fibonacci Numbers
# projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def even_fibonacci(n):
    sum_of_evens = 0
    prev = 1
    current = 2
    while current < n:
        if current % 2 == 0:
            sum_of_evens += current
        temp = current
        current += prev
        prev = temp
    return sum_of_evens


print(even_fibonacci(4000000))  # 4613732
