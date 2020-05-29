def solution(N):
    binary = bin(N).strip('0b').split('1')[1:-1]
    if not binary:
        return 0
    else:
        return len(max(binary))
  
print(solution(100000))