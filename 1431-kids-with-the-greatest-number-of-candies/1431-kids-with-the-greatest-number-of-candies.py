class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #find max element
        length = len(candies)
        maximum = candies[0]
        for i in range(1, length):
            if(maximum < candies[i]):
                maximum = candies[i]
        result = [False for i in range(length)]
        for i in range(length):
            if(candies[i] + extraCandies >= maximum):
                result[i] = True
        return result