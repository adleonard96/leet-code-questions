class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        largest_element = float("-inf")
        largest_element_count = 0
        count = 0
        
        current_element = float("-inf")

        for num in nums:
            if current_element == float("-inf"):
                count += 1
                current_element = num
                continue
            
            if num == current_element:
                count += 1
            else:
                if largest_element_count < count:
                    largest_element = current_element
                    largest_element_count = count

                current_element = num
                count = 1

        if largest_element_count < count:
            largest_element = current_element
            largest_element_count = count

        return largest_element

