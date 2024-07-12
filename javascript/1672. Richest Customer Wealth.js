/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0;
    let current = 0;
    for(let m = 0; m < accounts.length; m++){
        for(let n = 0; n < accounts[m].length; n++){
            current = accounts[m][n] + current;
        }
        if(current > max){
            max = current
        }
        current = 0
    }
    return max;
};