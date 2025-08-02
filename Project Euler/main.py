# Problem 1
# Calculate the sum of all multiples of 3 and 5 up until a limit
def multiple_sum(n):
    sum = 0
    for i in range(n):
        if not i % 3 or not i % 5:
            sum += i

    return sum


# Problem 2e
def generate_fibonacci(limit):
    current_number = 1
    previous_number = 1
    next_number = 1
    sequence = []

    # Create a fibonnaci sequence up to the limit given
    while next_number <= limit:
        sequence.append(next_number)
        if len(sequence) > 1:
            previous_number = sequence[-2]
        current_number = next_number
        next_number = current_number + previous_number
    
    return sequence

# Find the sum of all even numbers in the given array
def sum_even(array):
    sum = 0
    for number in array:
        if not number % 2:
            sum += number
    
    return sum


# Problem 3
def is_prime(number):
    for i in range(int(number / 2)):
        if not number % (i + 1) and i + 1 != 1:
            return False
        
    return True


def prime_factors(number):
    if is_prime(number):  # If a number is prime then it has no prime factors
        return [number]
    
    factors = []
    start = 2
    step = 1
    if number % 2:  # Can ignore all even numbers if root number is not even
        start = 3
        step = 2

    # Recursively find all prime factors of the number
    for i in range(start, int(number / 2), step):
        if not number % (i) and is_prime(i):
            factors.append(i)
            factors.extend(prime_factors(number / (i)))
            
            return factors


# Problem 4
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

# Find the highest palindrome that can be made by multiplying any 2 numbers
# Within the range given
def highest_palindrome(min, max):
    highest = 0
    for i in range(min, max):
        for k in range(min, max):
            product = i * k
            if is_palindrome(product) and product > highest:
                highest = product

    return highest
    

# Problem 5
# Find the lowest number that is a multiple of all numbers up to the given max
def lowest_multiple(max):
    number = 0
    while True:
        number += max
        for i in range(1, max + 1):
            if number % i:
                break

            # If this point is reached then the number is fully divisable 
            if i == max: 
                return number
    