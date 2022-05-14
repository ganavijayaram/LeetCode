class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        while(index < len(nums)):
            correct = nums[index]
            if(correct != nums[correct - 1]):
                temp = nums[correct - 1]
                nums[correct - 1] = correct
                nums[index] = temp
                pass
            else:
                index += 1
                
        for i in range(len(nums)):
            if(nums[i] != i+1):
                return nums[i]
            