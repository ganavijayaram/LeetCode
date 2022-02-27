class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(sorted(nums1))
        nums2 = list(sorted(nums2))
        start1 = 0
        start2 = 0
        length1 = len(nums1)
        length2 = len(nums2)
        c = []
        while(start1 < length1 and start2 < length2):
            if(nums1[start1] == nums2[start2]):
                c.append(nums1[start1])
                start1 += 1
                start2 += 1
            elif(nums1[start1] < nums2[start2]):
                start1 += 1
            else:
                start2 += 1
        return set(c)