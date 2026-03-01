function squaresWithThree(n) {
  let count = 0;
  for(let i=0; i<=n ;i++){
   let square = i*i;

   if(square.toString().includes("3")){
    count++;
   }
  }

  return count;
}