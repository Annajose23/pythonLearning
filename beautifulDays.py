
def beautifulDays(i,j,k):
    count = 0
    for item in range(i,j+1):
        item_rev = reverse_item(item)
        if item == item_rev:
            count += 1
        elif abs(item-item_rev)%k == 0:
            count += 1
    print(count)
    return count
        
def reverse_item(num):
    rev = 0
    while(num>0):
        last_digit = num%10
        rev = (rev * 10)+last_digit
        num = num//10
    return rev

beautifulDays(13,45,3)