/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var numToIndex = new Map();
    
    for(var i = 0; i < nums.length; i++) {
        if(numToIndex.has(target - nums[i])) {
            return [i, numToIndex.get(target - nums[i])];
        }
        
        numToIndex.set(nums[i], i);
    }
    
    return [];
};