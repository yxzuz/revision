"""
ทุกrecursive algorithm จะมีกฎ 3 ข้อ
1.Recursive algorithm ต้องมี base case
2.Recursive algorithm ต้องเปลี่ยนstate และเปลี่ยนไปเป็นbase case
3.Recursive algorithm ต้องเรียกตัวเอง
"""

def list_sum_no_recursion(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


# print(list_sum_no_recursion([1,3,5]))    ### Test No Recursion

def list_sum_recursion(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


print(list_sum_recursion([1,3,5]))       ### Test Recursion

### Test another Recursion
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[int(n)]
    else:
        return to_str(int(n / base), base) + convert_string[int(n % base)]


# print(to_str(1453, 10))
