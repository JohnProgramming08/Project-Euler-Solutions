// Problem 6
function sumOfSquaresAndSquareOfSum(limit) {
    limit++;
    let sum = 0;
    let sumOfSquares = 0;

    for (let i = 1; i < limit; i++) {
        sumOfSquares += i**2;
        sum += i
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

