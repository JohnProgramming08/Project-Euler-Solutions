// Problem 6
// Find the sum of the squares up to a limit
// And the square of the sum up to a limit
function sumOfSquaresAndSquareOfSum(limit) {
	limit++;
	let sum = 0;
	let sumOfSquares = 0;

	for (let i = 1; i < limit; i++) {
		sumOfSquares += i ** 2;
		sum += i;
	}

	return {
		sumOfSquares: sumOfSquares,
		squaredSum: sum ** 2,
	};
}

// Problem 7
function isPrime(number) {
	for (let i = 2; i < number ** 0.5 + 1; i++) {
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

// Problem 9
// Return the product of the pythagorean triplet which sums to a limit
function productOfTripletWhichSumsTo(limit) {
	for (let c = 3; c < limit; c++) {
		for (let b = 2; b < c; b++) {
			for (let a = 1; a < b; a++) {
				if (c ** 2 === a ** 2 + b ** 2 && a + b + c === limit) {
					return a * b * c;
				}
			}
		}
	}
	return `There are no pythagorean triplets, which sum to ${limit}`;
}

// Problem 10
// Return the sum of all primes up to a limit
function sumOfAllPrimes(limit) {
	let sum = 2;
	for (let i = 3; i < limit; i += 2) {
		if (isPrime(i)) {
			sum += i;
		}
	}
	return sum;
}
// Problem 16
// Return the sum of the digits of an exponent
function digitSum(base, power) {
	const digits = String(BigInt(base) ** BigInt(power));
	let sum = 0;
	for (let digit of digits) {
		sum += parseInt(digit);
	}

	return sum;
}
