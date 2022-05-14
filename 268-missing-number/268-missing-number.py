class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        while(index<len(nums)):
            if(nums[index] != index and nums[index] < len(nums)):
                temp = nums[nums[index]]
                nums[nums[index]] = nums[index]
                nums[index] = temp
            else:
                index += 1
                
        for i in range(len(nums)+1):
            if(i< len(nums) and nums[i] != i):
                return i
        return i