# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    number_frequency = {}
    for num in A:
        if num in number_frequency:
            number_frequency[num] += 1
        else:
            number_frequency[num] = 1
    number_frequency_sorted = sorted(number_frequency.items(), key=lambda kv: kv[1])
    return list(number_frequency_sorted[0])[0]
    
       
print(solution([9,3,9,3,9,7,7,12,9]))
