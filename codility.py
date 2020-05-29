#solution for the codility sample test to find the smallest integer missing in an array


def solution(A):
    items = list(set(A))
    print(items)
    items = list(filter(lambda item: item>0, items))
    print(items)
    if not items:
        return 1
    elif 1 not in items:
        return 1
    else:
        for index, item in enumerate(items[:-1]):
            if item + 1 != items[index + 1]:
                return item + 1
                break
        else:
            return (items[-1] + 1)

                

    
print(solution([2,3, -4]))