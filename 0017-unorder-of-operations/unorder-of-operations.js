function evaluate(numbers, operators) {
  let  result = numbers[0];
  let op_index = 0;

  for (let i = 1; i < numbers.length; i++){
    let operator = operators[op_index % operators.length]
    if (operator == "+"){
        result += numbers[i];
    }
    else if (operator == "-"){
        result -= numbers[i];
    }
    else if (operator == "*"){
        result *= numbers[i];
    }
    else if (operator == "/"){
        result /= numbers[i];
    }
    else if (operator == "%"){
        result %= numbers[i];
    }

    op_index++;
}
  return result;
}

//Test Stage
console.log(evaluate([5, 6, 7, 8, 9], ['+', '-']))