class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #Find max in an array
        result = []
        max = 0
        for item in candies:
            if(item > max):
                max = item
        print(max)
        for item in candies:
            if((item+extraCandies) >= max):
                result.append(True)
            else:
                result.append(False)
        
        return result

