function reverseSentence(sentence) {
    const words = sentence.split(/\s+/);  
    const reversedWords = words.reverse(); 
    const reversedSentence = reversedWords.join(" "); 
    
    return reversedSentence;
}

console.log(reverseSentence("world hello")); 