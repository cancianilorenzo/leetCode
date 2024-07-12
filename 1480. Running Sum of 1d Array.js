/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let numbers = [];
    numbers[0] = nums[0];
    for(let i = 1; i < nums.length; i++){
        numbers[i] = nums[i] + numbers[i-1];
    }
    return numbers;
};