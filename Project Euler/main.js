// Problem 6
// Find the sum of the squares up to a limit
// And the square of the sum up to a limit
function sumOfSquaresAndSquareOfSum(limit) {
    limit++;
    let sum = 0;
    let sumOfSquares = 0;

    for (let i = 1; i < limit; i++) {
        sumOfSquares += i**2;
        sum += i;
    };

    return {
        sumOfSquares: sumOfSquares,
        squaredSum: sum**2
    };
}

// Problem 7
function isPrime(number) {
    for (let i = 2; i < (number ** 0.5) + 1; i++) {
        if (number % i === 0 && number !== i) {
            return false;
        }
    }
    return true;
}

// Return the nth prime number
function nthPrimeNumber(n) {
    let count = 0;
    let number = 2;

    while (count < n) {
        if (isPrime(number)) {
            count++;
        }
        if (count === n) {
            return number;
        }
        number += 1;
    }
}

// Problem 8
// Return the highest product of 13 adjacent digits in a given number
function highestAdjacency(number) {
    let highest = 0;
    const adjacentNumbers = [];

    for (const char of number) {
        if (adjacentNumbers.length < 13) {
            adjacentNumbers.push(parseInt(char));
            continue;
        }

        let sum = 1;
        for (const number of adjacentNumbers) {
            sum = sum * number;
        }
        if (sum > highest) {
            highest = sum;
        }

        adjacentNumbers.shift();
        adjacentNumbers.push(parseInt(char));
    }

    return highest;
}