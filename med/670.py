def maximumSwap(num: int) -> int:
    str_num = str(num) # convert to string so that it can be indexed
    swap_index = -1 # set to a number that won't be found
    max_num_checked = 9 # largest number checked against
    for index, num in enumerate(str_num):
        if int(num) == 9: # if it's 9 it cant have a larger match
            continue

        search_string = str_num[index + 1:] # don't search numbers to the left of current index
        for k in range(max_num_checked, int(num), -1): # go backwards from max number.  
            if str(k) in search_string:
                swap_index = search_string.rindex(str(k)) + index + 1 # if a larger number is found then swapping it with current index will give largest possible number
                break;
        
        if swap_index > -1: # if a swap is found then swap and return
            str_num = list(str_num)
            swap = str_num[swap_index]
            str_num[swap_index] = str_num[index]
            str_num[index] = swap
            str_num = ''.join(str_num)
            return int(str_num)

        max_num_checked = int(num) + 1 # update max checked number because if it wasn't found when iterated then it won't be found again
    
    return int(str_num)


print(maximumSwap(1993))
