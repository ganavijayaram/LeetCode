class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev = arr[0]
        for i in range(1, len(arr)):
            if(prev > arr[i]):
                return i-1
            prev = arr[i]