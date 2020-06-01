# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    elem_obj = {}
    for element in A:
        print(element)
        if element in elem_obj:
            elem_obj[element] += 1
        else:
            elem_obj[element] = 1
    elem_obj_sorted = sorted(elem_obj.items(), key=lambda kv: kv[1], reverse= True)
    key, value = elem_obj_sorted[0]
    print(key,value, len(A))
    if value>len(A)/2:
        return key
    else:
        return -1

solution([2,3,4,3,3,3])