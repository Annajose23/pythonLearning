# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

solution([-3,1,2,-2,5,6])
