function jbelmu(text) {
    const words = text.split(' ');
    const result = [];

    for (let word of words) {
        let letters = word.split('');

        if (letters.length <= 2) {
            result.push(word);
            continue;
        }

        let firstLetter = letters.shift();
        let lastLetter = letters.pop();

        letters.sort();

        letters.unshift(firstLetter);         
        letters.push(lastLetter);              

        result.push(letters.join(''));
    }

    return result.join(' ');
}

// Test Stage
console.log(jbelmu("hello world"));