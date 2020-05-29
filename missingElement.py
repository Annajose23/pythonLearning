# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.
def solution(A):
   n = len(A)+1
   sum_elements = int(n*(n+1)/2)
   return sum_elements - sum(A)

print(solution([2,3,1,5]))