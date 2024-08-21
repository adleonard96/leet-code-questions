from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    # make a copy of nums1 so that order can be maintained with altering nums1
    nums1Copy = nums1.copy()
    
    # create positional tracker
    nums2_pos = 0
    nums1_pos = 0
    for num_index in range(len(nums1)):
        if nums1_pos != m and nums2_pos !=n:
            if(nums1Copy[nums1_pos] <= nums2[nums2_pos]):
                nums1[num_index] = nums1Copy[nums1_pos];
                nums1_pos += 1
            else:
                nums1[num_index] = nums2[nums2_pos]
                nums2_pos += 1
        elif nums1_pos == m:
            nums1[num_index] = nums2[nums2_pos]
            nums2_pos += 1
        elif nums2_pos == n:
            nums1[num_index] = nums1Copy[nums1_pos];
            nums1_pos += 1
