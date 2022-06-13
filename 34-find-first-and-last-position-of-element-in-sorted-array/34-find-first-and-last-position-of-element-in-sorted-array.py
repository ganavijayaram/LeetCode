class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        output = [-1, -1]
        if(len(nums) == 0):
            return output
        while(start <= end):
            mid = start + (end - start)//2
            if(target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        array_start = start
        if(start > len(nums)-1 or start < 0 or nums[start] != target):
            return output
        output[0] = start
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = start + (end - start)//2
            if(target < nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        array_end = end
        output[1] = end
        return (output)