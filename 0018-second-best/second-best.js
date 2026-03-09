function getLaptopCost(laptops, budget) {
    if (laptops[laptops.length - 2] <= budget) {
        return laptops[laptops.length - 2];
    }

    let result = 0;
    for (let price of laptops) {
        if (price <= budget) {
            if (result <= price) {
                result = price;
            }
        }
    }
    return result;
}
  
//Test Stage
console.log(getLaptopCost([1500, 2000, 1800, 1400], 1900))
console.log(getLaptopCost([2099, 1599, 1899, 1499], 1000))