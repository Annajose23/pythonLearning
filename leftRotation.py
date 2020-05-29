# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    length = len(A);
    if length == K:
        return A
    elif length == 0:
        return A
    else:
        K = K%length
        return (A[-K:]+ A[:-K])

print(solution([1,2,3,4],2))