class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        result = [i, j]
        for numOuter in nums:
            for numInner in nums:
                if ((numOuter + numInner) == target) and i != j:
                    print(numOuter, numInner, target, i, j)
                    return [i, j]
                j += 1
            i += 1
            j = 0
    

