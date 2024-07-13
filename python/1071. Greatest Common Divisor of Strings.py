class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenStr1 = len(str1)
        lenStr2 = len(str2)
        searchedLen = 0
        searchedString = ''
        if(lenStr1 > lenStr2):
            y = lenStr1
            x = lenStr2
        else:
            y = lenStr2
            x = lenStr1
        while(y):
            x, y = y, x % y
        searchedLen = abs(x)
        searchedString = str1[0:searchedLen]
        repetitionStr1 = len(str1)/searchedLen
        repetitionStr2 = len(str2)/searchedLen
        resultString1 = ''
        resultString2 = ''
        while(repetitionStr1 != 0):
            resultString1 += searchedString
            repetitionStr1 -= 1
        
        while(repetitionStr2 != 0):
            resultString2 += searchedString
            repetitionStr2 -= 1
        
        if(resultString1 == str1 and resultString2 == str2):
            return searchedString
        else:
            return ''



##Optimized
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lenStr1 = len(str1)
        lenStr2 = len(str2)
        searchedLen = 0
        if(lenStr1 > lenStr2):
            y = lenStr1
            x = lenStr2
        else:
            y = lenStr2
            x = lenStr1
        while(y):
            x, y = y, x % y
        searchedLen = abs(x)
        if(str1+str2 != str2+str1):
            return ''
        else:
            return str1[0:searchedLen]



