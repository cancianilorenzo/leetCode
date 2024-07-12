class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            currentStr = ''
            if(i % 3 == 0):
                currentStr += 'Fizz'
            if(i % 5 == 0):
                currentStr += 'Buzz'
            if(not currentStr):
                currentStr += str(i)
            result.append(currentStr)
        return result