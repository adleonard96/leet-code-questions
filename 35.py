def searchInsert(nums, target: int) -> int:
    mid = len(nums)//2
    lower = 0
    upper = len(nums)
    
    while lower != upper and lower+1 != upper:
        if target < nums[mid]:
            upper = mid
            mid = lower + ((upper - lower) // 2)
        elif target > nums[mid]:
            lower = mid  
            mid = lower + ((upper - lower) // 2)
        elif target == nums[mid]:
            return mid
    
    if nums[lower] < target:
        return upper
    else: return lower

nums = [1,3,5,6]

print(searchInsert(nums, 7))