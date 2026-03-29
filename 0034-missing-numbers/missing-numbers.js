function findMissingNumbers(arr) {
    if (!arr || arr.length === 0) {
        return [];
    }
    
    const largestNum = Math.max(...arr); 
    const numSet = new Set(arr);
    
    const missing = [];
    for (let i = 1; i <= largestNum; i++) {
        if (!numSet.has(i)) {
            missing.push(i);
        }
    }
    
    return missing;
}