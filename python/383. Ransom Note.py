class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        
        for char in magazine:
            currentCount = 0
            if char in magazineDict:
                magazineDict[char] += 1
            else:
                magazineDict[char] = 1

        for char in ransomNote:
            if char in magazineDict and magazineDict[char] > 0:
                magazineDict[char] -= 1
            else:
                return False
        return True

