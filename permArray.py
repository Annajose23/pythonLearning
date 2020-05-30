
def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    if A == list(range(1,len(A)+1)):
        return 1
    else:
        return 0
    


print(solution([4,1,2,3]))