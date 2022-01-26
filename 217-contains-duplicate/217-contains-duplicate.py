'''Using Array'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False

''' Brute Force '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length-1):
            for j in  range(i+1, length):
                if(nums[i] == nums[j]):
                    return True
        return False
