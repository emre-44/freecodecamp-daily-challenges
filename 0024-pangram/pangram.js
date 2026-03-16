function isPangram(sentence, letters) {

    const sentenceLetters = new Set();
    
    for (let i = 0; i < sentence.length; i++) {
        const char = sentence[i];
        if (/[a-zA-Z]/.test(char)) {
            sentenceLetters.add(char.toLowerCase());
        }
    }
    
    const lettersCheck = new Set(letters.split(''));
    
    return JSON.stringify([...lettersCheck].sort()) === 
           JSON.stringify([...sentenceLetters].sort());
}

// Test Stage
console.log(isPangram("Hello World!", "helowrd"));  
