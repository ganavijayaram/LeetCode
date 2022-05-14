class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(1, len(nums) + 1):
            xor ^= i
        
        xor1 = nums[0]    
        for i in range(1, len(nums)):
            xor1 ^= nums[i]
            
        return(xor ^ xor1)