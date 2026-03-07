function decode(s) {
    const stack = [];
    
    for (const char of s) {
        if (char === ')') {
            const temp = [];
            while (stack.length > 0 && stack[stack.length - 1] !== '(') {
                temp.push(stack.pop());
            }
            stack.pop();
            stack.push(...temp);
        } else {
            stack.push(char);
        }
    }   
    return stack.join('');
}

//Test Stage
console.log(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"));