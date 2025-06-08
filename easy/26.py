def removeDuplicates(nums: List) -> int:
    pointer = 0
    for i in range(1, len(nums)):
        if nums[pointer] < nums[i]:  
            nums[pointer + 1] = nums[i]
            pointer += 1

    return pointer + 1

print(removeDuplicates([1,1,2]))