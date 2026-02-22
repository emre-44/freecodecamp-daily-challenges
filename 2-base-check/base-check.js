function isValidNumber(n, base) {

  const validChars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  const allowedChars = validChars.slice(0, base);

  const nUpper = n.toUpperCase();

      for (let i = 0; i < nUpper.length; i++) {
        if (!allowedChars.includes(nUpper[i])) {
            return false;
        }
    }
    
    return true;
}

// Test Stage
console.log(isValidNumber("1010", 2));    // true
console.log(isValidNumber("102", 2));     // false
console.log(isValidNumber("1A3F", 16));   // true