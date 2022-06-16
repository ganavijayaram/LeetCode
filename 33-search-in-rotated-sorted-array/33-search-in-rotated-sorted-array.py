class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end-start)//2
            if(nums[mid] == target):
                return mid
            if(nums[start] > nums[mid]):
                #1st part uneven
                #2nd part ascending
                if(target > nums[mid] and target <= nums[end]):
                    start = mid + 1
                else:
                    end = mid - 1
                pass
            else:
                #1st part ascending
                if(target >= nums[start] and target < nums[mid]):
                    end = mid - 1
                #2nd part uneven 
                else:
                    start = mid + 1
        return -1
                
            