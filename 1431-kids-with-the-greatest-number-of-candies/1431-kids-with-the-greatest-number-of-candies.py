class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = candies[0]
        output = []
        for i in candies:
            if(i > maximum):
                maximum = i
        for i in candies:
            if(i + extraCandies >= maximum):
                output.append(True)
            else:
                output.append(False)
        return output