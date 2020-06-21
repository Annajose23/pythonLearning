def commonElements(A,B):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(A) and p2 < len(B):
        if A[p1] == B[p2]:
            result.append(A[p1])
            p1 = p1 + 1
            p2 = p2 + 1
        elif A[p1] > B[p2]:
            p2 = p2 + 1
        else:
            p1 = p1 + 1
    print(result)
    return result

commonElements([1,3,5,6,7,8], [1,2,3,4,5,8])