# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_diff = abs(head - tail)
    for item in range(1, len(A)-1):
        head = head + A[item]
        tail = tail - A[item]
        diff = abs(head - tail)
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(solution([3,1,2,4,3]))