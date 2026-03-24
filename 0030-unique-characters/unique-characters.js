function allUnique(s) {
    let letters = s.split('');
    
    for (let i = 0; i < letters.length; i++) {
        let current = letters[i];
        let remaining = letters.slice(0, i).concat(letters.slice(i + 1));
        if (remaining.includes(current)) {
            return false;
        }
    }
    return true;
}