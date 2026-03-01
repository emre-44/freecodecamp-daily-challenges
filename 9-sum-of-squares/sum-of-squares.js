function sumOfSquares(n) {
    let total = 0;
  for(let i=0;i<=n;i++){
    total += i*i;
  }
  return total;
}

//Test Stage
console.log(sumOfSquares(5))