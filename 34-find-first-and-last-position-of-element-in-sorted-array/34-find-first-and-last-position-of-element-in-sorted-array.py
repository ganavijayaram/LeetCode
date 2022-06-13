class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        output = []
        if(len(nums) == 0):
            output.append(-1)
            output.append(-1)
            #print(output)
            return output
        while(start <= end):
            mid = start + (end - start)//2
            if(target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
        array_start = start
        if(start > len(nums)-1 or start < 0 or nums[start] != target):
            output.append(-1)
            output.append(-1)
            #print(output)
            return output
        output.append(start)
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = start + (end - start)//2
            if(target < nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        array_end = end
        output.append(end)
        return (output)