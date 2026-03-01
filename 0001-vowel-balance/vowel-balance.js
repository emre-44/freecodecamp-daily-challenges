function isBalanced(s) {
    /*
    Checks if number of vowels in first half equals second half
    If odd length, ignore the center character
    */
    
    s = s.replaceAll(" ", "");
    let length = s.length;
    let middle = Math.floor(length / 2);
    
    let word1, word2;
    
    if (length % 2 === 1) {  
        word1 = s.slice(0, middle);
        word2 = s.slice(middle + 1);
        console.log(`Odd length! Middle character '${s[middle]}' is ignored`);
    } else {  
        word1 = s.slice(0, middle);
        word2 = s.slice(middle);
    }
    
    const vowels = "aeiou";
    
    let count1 = 0;
    let count2 = 0;
    
    for (let letter of word1.toLowerCase()) {
        if (vowels.includes(letter)) {
            count1++;
        }
    }
    
    for (let letter of word2.toLowerCase()) {
        if (vowels.includes(letter)) {
            count2++;
        }
    }
    
    console.log(`Word: '${s}'`);
    console.log(`First half: '${word1}' (${count1} vowels)`);
    console.log(`Second half: '${word2}' (${count2} vowels)`);
    
    if (count1 === count2) {
        console.log("Vowel balanced!\n");
        return true;
    } else {
        console.log("Not vowel balanced!\n");
        return false;
    }
}