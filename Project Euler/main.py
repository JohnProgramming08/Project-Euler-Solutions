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
            # 4 diagonal numbers to the bottom right
            if i < len(row) - 3 and k < len(numbers) - 3:
                diagonal_adjacency_right = [
                    number,
                    numbers[k - 1][i + 1],
                    numbers[k - 2][i + 2],
                    numbers[k - 3][i + 3],
                ]
                adjacancies.append(diagonal_adjacency_right)

            # 4 horizontal numbers to the right in a row
            if i < len(row) - 3:
                horizontal_adjacency = [
                    number,
                    row[i + 1],
                    row[i + 2],
                    row[i + 3],
                ]
                adjacancies.append(horizontal_adjacency)

            # Cant go back by 3 columns if we are not at least at the 4th column
            # 4 digonal numbers ot the bottom left
            if i > 2 and k < len(numbers) - 3:
                diagonal_adjacency_left = [
                    number,
                    numbers[k - 1][i - 1],
                    numbers[k - 2][i - 2],
                    numbers[k - 3][i - 3],
                ]
                adjacancies.append(diagonal_adjacency_left)

            # 4 vertical numbers down in a column
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


# Problem 14
# Return the longest chain in collatz conjecture up to a start number of limit
def longest_chain_starter(limit):
    highest_length = 0
    longest_starter = 0
    checked = {}

    for i in range(2, limit):
        current = i
        length = 0
        # Even: n / 2, odd: 3n + 1
        while current != 1:
            # Avoid calculating for numbers that are already checked
            if current in checked:
                length += checked[current]
                break

            # Apply collatz ruless
            if not current % 2:
                current //= 2
            else:
                current = (current * 3) + 1

            length += 1

        checked[i] = length
        if length > highest_length:
            highest_length = length
            longest_starter = i

    return longest_starter


# Problem 15
# Return the factorial of a number
def factorial(number):
    if number == 1:
        return number

    product = factorial(number - 1)
    return number * product


# Return the number of paths to get from top left to right in a grid
# Of size x size, no left or up movements
# Using the binomial formula
def number_of_paths(size):
    return factorial(size * 2) / (factorial(size) ** 2)


# Problem 21
# Return the sum of the divisors of a number
def divisor_sum(number):
    divisor_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if not number % i and number // i != i:
            divisor_sum += i
            divisor_sum += number // i
        elif not number % i:
            divisor_sum += i

    return divisor_sum


# Return the sum of all amicable numbers less than n
def amicable_number_sum(n):
    amicable_numbers = []

    for i in range(1, n):
        sum1 = divisor_sum(i)
        sum2 = divisor_sum(sum1)
        # Avoid duplicate amicable numbers in the list
        if sum2 == i and i not in amicable_numbers and sum2 != sum1:
            amicable_numbers.append(sum1)
            amicable_numbers.append(sum2)

    return sum(amicable_numbers)


# Problem 22
# Sort the file of names alphabetically
def name_sort(file_name):
    with open(file_name, "r") as file:
        contents = file.read()
        names = sorted(contents.split(","))
        return names


# Return the sum of all name scores
def sum_name_scores(names):
    sum = 0
    for i in range(len(names)):
        name = names[i][1:-1].lower()

        # Get the sum of the alphabetical positions of letters in each name
        alphabetical_value = 0
        for char in name:
            alphabetical_value += ord(char) - 96

        sum += (i + 1) * alphabetical_value

    return sum


# Problem 23
# Return the sum of all abundant numbers up to a limit
def abundant_numbers(limit):
    numbers = []
    for i in range(1, limit):
        if divisor_sum(i) > i:
            numbers.append(i)

    return numbers


# Return whether or not a number can be written as the sum of 2 abundant numbers
def is_sum_of_abundant_numbers(number, all_abundant_numbers):
    for abundant_number in all_abundant_numbers:
        # No 2 numbers greater than half a number can sum to said number
        if abundant_number > number // 2:
            return False
        elif number - abundant_number not in all_abundant_numbers:
            continue

        return True


# Return the sum of all numbers that aren't the sum of 2 abundant numbers
def sum_of_non_abundant_summable_numbers():
    numbers = set(abundant_numbers(28123))
    sum = 0
    for i in range(1, 28123):
        if not is_sum_of_abundant_numbers(i, numbers):
            sum += i

    return sum


# Problem 24
# Return the nth lexicographic permutation
def lexicographic_permutation(n):
    numerator = n - 1
    digits = ""
    possible_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Use the factorial of each number to determine which digit it should be
    for i in range(9, 0, -1):
        index = numerator // factorial(i)
        digits += str(possible_digits[index])
        possible_digits.pop(index)
        numerator = numerator % factorial(i)

    # Only one number should remain
    digits += str(possible_digits[0])

    return int(digits)


# Problem 25
# Return the index of the first fibonacci number with n digits
def nth_digit_fibonacci_number(n):
    current_number = 1
    previous_number = 1
    next_number = 1
    sequence = []

    # Create a fibonnaci sequence up to the limit given
    while len(str(next_number)) != n:
        sequence.append(next_number)
        if len(sequence) > 1:
            previous_number = sequence[-2]
        current_number = next_number
        next_number = current_number + previous_number

    # As only one 1 was added to the sequence and next_number isnt in sequence
    return len(sequence) + 2
