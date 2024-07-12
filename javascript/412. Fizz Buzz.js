/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let result = [];
    for(let i = 1; i < n+1; i++){
        let currentString = '';
        if(i % 3 === 0){
            currentString += 'Fizz';
        }
        if(i % 5 === 0){
            currentString += 'Buzz';
        }
        if(!currentString){
            currentString = i.toString();
        }
        result.push(currentString);
    }
    return result;
};