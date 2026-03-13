function generateHex(color) {
    if (!["red", "green", "blue"].includes(color)) {
        return "Invalid color";
    }
    
    while (true) {
        let r = Math.floor(Math.random() * 256);  
        let g = Math.floor(Math.random() * 256);
        let b = Math.floor(Math.random() * 256);
        
        let condition;
        
        if (color === "red") {
            condition = r > g && r > b;
        } else if (color === "green") {
            condition = g > r && g > b;
        } else if (color === "blue") {
            condition = b > r && b > g;
        }
        
        if (condition) {            
            return "" + 
                r.toString(16).padStart(2, '0').toUpperCase() +
                g.toString(16).padStart(2, '0').toUpperCase() +
                b.toString(16).padStart(2, '0').toUpperCase();
        }
    }
}