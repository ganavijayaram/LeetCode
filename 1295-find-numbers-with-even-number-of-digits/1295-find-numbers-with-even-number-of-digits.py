class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        tot_count = 0
        for i in nums:
            count = 0
            while(i):
                count += 1
                i //= 10
            if(count % 2 == 0):
                tot_count += 1
        return tot_count