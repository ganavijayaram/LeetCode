class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        nums.sort()
        start = 0
        end = 1
        while(end < length):
            if(nums[start] == nums[end]):
                return True
            else:
                start += 1
                end += 1
        return False