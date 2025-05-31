def removeDuplicates(nums) -> int:
    return list(set(nums))

print(sorted(removeDuplicates([1,1,2])))