class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0 
        j = 0
        found = False
        while not found:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

            if i >= len(nums1) or j >= len(nums2):
                return -1