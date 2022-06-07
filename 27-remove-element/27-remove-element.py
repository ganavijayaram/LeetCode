class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        while(i < (len(nums)-count)):
            if(nums[i] == val):
                for j in range(i+1, (len(nums)-count)):
                    nums[j-1] = nums[j]
                count += 1
            else:
                i += 1
        return(len(nums) - count)