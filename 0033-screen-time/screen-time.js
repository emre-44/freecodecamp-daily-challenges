function tooMuchScreenTime(hours) {
    let sum = 0;
    
    for(let i = 0; i < hours.length; i++) {
        if(hours[i] >= 10) {
            return true;
        }
        
        if(i <= hours.length - 3 && (hours[i] + hours[i+1] + hours[i+2]) / 3 >= 8) {
            return true;
        }
        
        sum += hours[i];
    }
    
    if(sum / 7 >= 6) {
        return true;
    }
    
    return false;
}