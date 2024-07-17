##Naive approach
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashNum1 = {}
        hashNum2 = {}
        diff12 = []
        diff21 = []
        for num in nums1:
            if num in hashNum1:
                currentValue = hashNum1[num] + 1
                hashNum1.update({num: currentValue})
                currentValue = 0
            hashNum1.update({num: 1})
        
        for num in nums2:
            if num not in hashNum1 and num not in diff21:
                diff21.append(num)
            if num in hashNum2:
                currentValue = hashNum2[num] + 1
                hashNum1.update({num: currentValue})
                currentValue = 0
            hashNum2.update({num: 1})
        
        for num in hashNum1:
            if num not in hashNum2 and num not in diff12:
                diff12.append(num)

        return[diff12, diff21]


#Optimized approach
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []]

        for i in s1:
            if i not in s2:
                ans[0].append(i)
        
        for i in s2:
            if i not in s1:
                ans[1].append(i)
        
        return ans
