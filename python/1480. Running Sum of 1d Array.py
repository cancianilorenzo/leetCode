class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[0])
        i = 1
        nums.pop(0)
        for num in nums:
            result.append(num + result[i-1])
            i += 1
        return result