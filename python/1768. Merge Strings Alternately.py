class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        outputString = ''
        selector = 0
        while (len(word1) != 0 and len(word2) != 0):
            if((selector & 1) == 0):
                outputString += word1[0]
                word1 = word1[1:]
                selector += 1
            else:
                outputString += word2[0]
                word2 = word2[1:]
                selector -= 1
        outputString += word2
        outputString += word1
        return outputString

        #Time complexity --> O(n+m)
        #Space complexity --> O(1)

        #Time spent 17.41
                
