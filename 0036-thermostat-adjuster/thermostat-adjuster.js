function adjustThermostat(temp, target) {

    if (temp < target){
        return "heat"
    }
    else if (target < temp){
        return "cool"
    }

    else{
        return "hold"
    }
}
