# Problem 1
# Calculate the sum of all multiples of 3 and 5 up until a limit
def multiple_sum(n):
    sum = 0
    for i in range(n):
        if not i % 3 or not i % 5:
            sum += i

    return sum


# Problem 2
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


# Problem 11
def find_product(array):
    product = 1
    for i in array:
        product *= i

    return product


# Return the highest product of 4 adjacent numbers
def highest_adjacency(numbers):
    highest = 0

    # k points to the row, i points to the column
    for k in range(len(numbers)):
        row = numbers[k]
        for i in range(len(row)):
            number = row[i]
            adjacancies = []

            # Cant have 4 adjacent diagonal numbers after the last 3 columns
            # Or rows
            if i < len(row) - 3 and k < len(numbers) - 3:
                diagonal_adjacency_right = [
                    number,
                    numbers[k - 1][i + 1],
                    numbers[k - 2][i + 2],
                    numbers[k - 3][i + 3],
                ]
                adjacancies.append(diagonal_adjacency_right)

            if i < len(row) - 3:
                horizontal_adjacency = [
                    number,
                    row[i + 1],
                    row[i + 2],
                    row[i + 3],
                ]
                adjacancies.append(horizontal_adjacency)

            # Cant go back by 3 columns if we are not at least at the 4th column
            if i > 2 and k < len(numbers) - 3:
                diagonal_adjacency_left = [
                    number,
                    numbers[k - 1][i - 1],
                    numbers[k - 2][i - 2],
                    numbers[k - 3][i - 3],
                ]
                adjacancies.append(diagonal_adjacency_left)

            if k < len(numbers) - 3:
                vertical_adjacency = [
                    number,
                    numbers[k + 1][i],
                    numbers[k + 2][i],
                    numbers[k + 3][i],
                ]
                adjacancies.append(vertical_adjacency)

            # Find the highest product
            for list in adjacancies:
                if find_product(list) > highest:
                    highest = find_product(list)

    return highest


# Problem 12
# Return the number of factors a number has
def number_of_factors(number):
    count = 1
    for i in range(2, int((number**0.5) + 1)):
        if not number % i:
            count += 2

    return count


# Return the first triangle number with over n factors
def first_triangle_number(number):
    current_number = 0
    triangle_number = 0

    while True:
        current_number += 1
        triangle_number += current_number

        if number_of_factors(triangle_number) > number:
            return triangle_number


# Problem 13
# Return the first 10 digits of the sum of n 50 digit numbers
def first_ten_digits(number):
    index = 0
    sum = 0

    # Add together sections of 50 digits
    while index < len(number):
        sum += int(number[index : index + 50])
        index += 50

    return str(sum)[0:10]
