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