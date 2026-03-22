function parseRomanNumeral(numeral) {
    const romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    let total = 0;
    const n = numeral.length;

    for (let i = 0; i < n; i++) {
        const currentValue = romanValues[numeral[i]];

        if (i + 1 < n && currentValue < romanValues[numeral[i + 1]]) {
            total -= currentValue;
        } else {
            total += currentValue;
        }
    }
    
    return total;
}

// Test
console.log(parseRomanNumeral("XXVI"));