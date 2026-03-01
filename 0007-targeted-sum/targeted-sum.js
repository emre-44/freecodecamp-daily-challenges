function findTarget(arr, target) {
  const seen = new Map();

    for (const [index, num] of arr.entries()) {
        const complement = target - num;
        
        if (seen.has(complement)) {
            return [seen.get(complement), index].sort((a, b) => a - b);
        }
        
        seen.set(num, index);
    }
    
    return "Target not found";
}
