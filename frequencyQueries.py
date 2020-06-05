from collections import defaultdict
n = int(input())

a = defaultdict(int) # num:cnt
b = defaultdict(int) # cnt: how many nums have this cnt

for tc in range(n):
    op, data = map(int, input().strip().split())

    if op == 1:
        # insert
        b[a[data]] -= 1
        a[data]+=1
        b[a[data]] += 1

    elif op == 2:
        # delete
        if data in a:
            b[a[data]] -= 1
            a[data] -= 1
            b[a[data]] += 1

        a[data]  = 0 if a[data] < 0 else a[data]

    else:
        # check if any key in b = data and has count > 0         
        print('1' if data in b and b[data] > 0  else '0')