function decode(message, shift) {
    let decoded = "";
    
    for (let i = 0; i < message.length; i++) {
        let char = message[i];
        
        if (/[a-zA-Z]/.test(char)) {
            if (char === char.toUpperCase()) {
                let charCode = char.charCodeAt(0) - 65;
                charCode = (charCode - shift) % 26;
                if (charCode < 0) charCode += 26;
                decoded += String.fromCharCode(charCode + 65);
            } else {
                let charCode = char.charCodeAt(0) - 97;
                charCode = (charCode - shift) % 26;     
                if (charCode < 0) charCode += 26;      
                decoded += String.fromCharCode(charCode + 97); 
            }
        } else {
            decoded += char;
        }
    }
    
    return decoded;
}

//Test Stage
console.log(decode("Xlmw mw e wigvix qiwweki.", 4));