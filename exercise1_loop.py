list1 = [14,17,23,33]
list2 = [13,16,17,35]

def common_number(list_a, list_b):
    for i in list_a:
        if i in list_b:
            return i
    return "There is no common number"

print(common_number(list1,list2))