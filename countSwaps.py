def countSwaps(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count = count + 1
    print("Array is sorted in", count,"swaps.")
    print("First Element:" ,arr[0])
    print("Last Element:" , arr[n-1])

countSwaps([3,2,1])