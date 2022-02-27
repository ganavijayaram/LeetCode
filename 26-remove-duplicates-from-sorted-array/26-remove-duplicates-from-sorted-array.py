class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if(length == 1):
            return 1
        start = 0
        end = 1
        while(end != (length)):
            if(nums[start] != nums[end]):
                nums[start+1] = nums[end]
                start += 1
            end += 1
        return (start+1)