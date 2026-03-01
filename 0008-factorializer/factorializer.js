function factorial(n) {
  if (n === 0) {
    return 1;  
  }
  
  let result = 1;  
  
  for (let i = 1; i <= n; i++) {  
    result = result * i;  
  }
  
  return result;
}

//Test Stage
console.log(factorial(0));
console.log(factorial(5));