function isValidIPv4(ipv4) {
    if (ipv4.split('.').length - 1 !== 3) {
        return false;
    }
    
    const parts = ipv4.split('.');
    
    if (parts.length !== 4) {
        return false;
    }
    
    for (let part of parts) {
        if (!part) {
            return false;
        }
        
        if (part.length > 1 && part[0] === '0') {
            return false;
        }
        
        if (!/^\d+$/.test(part)) {
            return false;
        }
        
        const num = parseInt(part, 10);
        
        if (num < 0 || num > 255) {
            return false;
        }
    }
    
    return true;
}