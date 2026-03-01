function fibonacciSequence(startSequence, length) {

    if (length < 0) {
        return "Length cannot be negative!";
    }
    if (length === 0) {
        return [];
    }
    if (!Array.isArray(startSequence) || startSequence.length < 2) {
        return "Start sequence must be an array with at least 2 elements!";
    }

    let result = [...startSequence];

    for (let i = 2; i < length; i++) {
        result.push(result[i-1] + result[i-2]);
    }

    return result.slice(0, length);
}

// Test Stage
console.log(fibonacciSequence([0, 1], 12));