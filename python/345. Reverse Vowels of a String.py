class Solution:
    def reverseVowels(self, s: str) -> str:
        target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        volwesArray = []
        result = ''
        for char in s:
            if(char in target):
                volwesArray.insert(0, char)
        for char in s:
            if(char in target):
                result += volwesArray[0]
                volwesArray.pop(0)
            else:
                result += char
        return result
