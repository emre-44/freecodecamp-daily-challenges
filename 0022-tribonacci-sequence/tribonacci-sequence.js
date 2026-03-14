function tribonacciSequence(startSequence, length) {
    if (!startSequence || startSequence.length === 0) {
        return [];
    }
    
    let result = [...startSequence];
    
    while (result.length < length) {
        let nextValue = result[result.length - 1] + 
                        result[result.length - 2] + 
                        result[result.length - 3];
        result.push(nextValue);
    }

    return result.slice(0, length);
}

// Test Stage
console.log(tribonacciSequence([0, 0, 1], 20));
