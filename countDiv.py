# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    count = 0
    for item in range(A,B+1):
        if item % K == 0:
            count += 1
    return count


print(solution(6,11,2))