class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        arr = []
        isEven = length % 2 == 0
        need = length // 2
        # if isEven:
        need += 1

        counter_1 = 0
        counter_2 = 0
        while len(arr) < need:
            valid_counter2 = counter_2 < len(nums2)
            valid_counter1 = counter_1 < len(nums1)
            if valid_counter2 and valid_counter1 and nums2[counter_2] <= nums1[counter_1]:
                arr.append(nums2[counter_2])
                counter_2 += 1
            elif valid_counter2 and valid_counter1 and nums2[counter_2] > nums1[counter_1]:
                arr.append(nums1[counter_1])
                counter_1 += 1
            elif valid_counter2:
                arr.append(nums2[counter_2])
                counter_2 += 1
            else:
                arr.append(nums1[counter_1])
                counter_1 += 1

        if not isEven:
            return arr[-1]
        else:
            return (arr[-1] + arr[-2]) / 2