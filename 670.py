def maximumSwap(num: int) -> int:
    str_num = str(num)
    swap_index = -1
    max_num_checked = 9
    for index, num in enumerate(str_num):
        if int(num) == 9:
            continue

        search_string = str_num[index + 1:]
        for k in range(max_num_checked, int(num), -1):
            if str(k) in search_string:
                swap_index = search_string.rindex(str(k)) + index + 1
                break;
        
        if swap_index > -1:
            str_num = list(str_num)
            swap = str_num[swap_index]
            str_num[swap_index] = str_num[index]
            str_num[index] = swap
            str_num = ''.join(str_num)
            return int(str_num)

        max_num_checked = int(num) + 1
    
    return int(str_num)


print(maximumSwap(1993))