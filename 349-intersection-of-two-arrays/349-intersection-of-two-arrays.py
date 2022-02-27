class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D = {}
        for i in nums1:
            if(i not in D):
                D[i] = 1
        c = []
        
        for i in nums2:
            if(i in D):
                c.append(i)
        return set(c)