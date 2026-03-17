function repeatVowels(str) {
    const vowels = "aeiouAEIOU";
    let count = 0;
    let result = "";
    
    for (let i = 0; i < str.length; i++) {
        const ch = str[i];
        
        if (vowels.includes(ch)) {
            count++;
            if (count === 1) {
                result += ch;
            } else {
                result += ch + ch.toLowerCase().repeat(count - 1);
            }
        } else {
            result += ch;
        }
    }
    
    return result;
}