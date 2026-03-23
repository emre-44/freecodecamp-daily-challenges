function buildAcronym(s) {
    const words = s.split(" ");
    const unless = ["a", "for", "an", "and", "by", "of"];
    let result = "";
    
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if (i === 0 || !unless.includes(word.toLowerCase())) {
            result += word[0].toUpperCase();
        }
    }
    
    return result;
}