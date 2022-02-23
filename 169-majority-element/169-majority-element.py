class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        D = {}
        total = len(nums)/2
        for i in nums:
            if(i in D):
                D[i] += 1
            else:
                D[i] = 1
        for key in D.keys():
            if(D[key] > total):
                return key