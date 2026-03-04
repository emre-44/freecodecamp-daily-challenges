function isUnnaturalPrime(n) {
    if  (n == 0 || n == 1 || n == -1){
      return false;
    }

    else if ( n > 0){
      for (let i=2; i<=(n/2)+1;i++){
        if (n % i == 0){
          return false;
        }
      }
    }

    else if (n < 0){
      n = Math.abs(n);
       for (let i=2; i<=(n/2)+1;i++){
        if (n % i == 0){
          return false;
        }
    }
  }  
  return true
}