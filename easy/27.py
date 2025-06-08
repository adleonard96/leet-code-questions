def removeElement(self, nums: List[int], val: int) -> int:
    element = 0
    needs_replaced = []

    for i in range(len(nums)):
        if nums[i] == val:
            needs_replaced.append(i)
        else:
            if len(needs_replaced) > 0:
                nums[needs_replaced[0]] = nums[i]
                needs_replaced.append(i)
                needs_replaced = needs_replaced[1:]
            element += 1

    return element
            
        