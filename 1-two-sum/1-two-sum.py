class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if(length == 2):
            return (0, 1)
        for i in range(length-1):
            for j in range(i+1, length):
                if(nums[i] + nums[j] == target):
                    return (i,j)