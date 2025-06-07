def addBinary(a: str, b: str) -> str:
    index_a = len(a) - 1
    index_b = len(b) - 1
    carry = 0
    answer = []

    while(index_a >= 0 and index_b >= 0):
        answer_bit, carry = add_binary(int(a[index_a]), int(b[index_b]), carry)
        answer.append(answer_bit)
        index_a -= 1
        index_b -= 1

    while(index_a >= 0):
        answer_bit, carry = add_binary(int(a[index_a]), 0, carry)
        index_a -= 1
        answer.append(answer_bit)
    
    while(index_b >= 0):
        answer_bit, carry = add_binary(0, int(b[index_b]), carry)
        index_b -= 1
        answer.append(answer_bit)

    if carry > 0:
        answer.append(1)

    ans_str = ""
    while answer:
        ans_str += str(answer.pop())

    return ans_str

    

def add_binary(num1, num2, carry):
    if num1 == 1 and num2 == 1:
        return 0 + carry, 1
    elif (num1 == 1 or num2 == 1) and carry == 1:
        return 0, 1
    elif (num1 == 1 or num2 == 1) and carry == 0:
        return 1, 0
    elif (num1 == 0 and num2 == 0) and carry == 1:
        return 1, 0
    else:
        return 0, 0


print(addBinary("1010", "1011"))