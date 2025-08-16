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

// Problem 17
// Sum of letters to represent numbers from 1 to 1000
function letterSum() {
	let characterSum = 0;
	const digitToWord = {
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
		20: 'twenty',
		30: 'thirty',
		40: 'forty',
		50: 'fifty',
		60: 'sixty',
		70: 'seventy',
		80: 'eighty',
		90: 'ninety',
	};

	// Convert the number to words and add the length of the word variant
	for (let i = 1; i < 1001; i++) {
		let words = '';

		if (i === 1000) {
			words = 'onethousand';
		} else {
			// Hundreds column
			const hundreds = Math.floor(i / 100);
			if (hundreds > 0) {
				words += digitToWord[hundreds] + 'hundred';
			}

			// Tens column including teens
			const tens = Math.floor(i / 10) - hundreds * 10;
			if (tens === 1) {
				words += digitToWord[i % 100];
			} else if (tens > 1) {
				words += digitToWord[tens * 10];
			}

			// Ones column only if there is no teen
			const ones = i % 10;
			if (ones > 0 && tens !== 1) {
				words += digitToWord[ones];
			}

			// Should and be added or not
			if (hundreds > 0 && (tens > 0 || ones > 0) && i > 9) {
				words += 'and';
			}
		}
		characterSum += words.length;
	}

	return characterSum;
}

// Problem 18
// Find the path with the maximum sum through brute force
function maximumSum(pyramid, row, index) {
	// Base case
	if (row === pyramid.length - 1) {
		return pyramid[row][index];
	}

	const rightSum = maximumSum(pyramid, row + 1, index + 1);
	const leftSum = maximumSum(pyramid, row + 1, index);

	if (leftSum > rightSum) {
		return leftSum + pyramid[row][index];
	} else {
		return rightSum + pyramid[row][index];
	}
}
