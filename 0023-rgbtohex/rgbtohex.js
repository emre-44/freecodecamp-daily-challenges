function rgbToHex(rgb) {

    let hexCodes = rgb.replace("rgb(", "").replace(")", "").split(", ");
    let r = parseInt(hexCodes[0]);
    let g = parseInt(hexCodes[1]);
    let b = parseInt(hexCodes[2]);
    
    let hexColor = "#" + 
        r.toString(16).padStart(2, '0') +
        g.toString(16).padStart(2, '0') +
        b.toString(16).padStart(2, '0');
    
    return hexColor;
}

// Test Stage
console.log(rgbToHex("rgb(255, 255, 255)"));  