function findDuplicates(arr) {
  const seen = new Set();
  const duplicates = new Set();
  
  for (const num of arr) {
    if (seen.has(num)) {
      duplicates.add(num);
    } else {
      seen.add(num);
    }
  }
  return Array.from(duplicates).sort((a, b) => a - b);
}

// Test Stage
console.log(findDuplicates([1, 2, 3, 4, 1, 2])); 