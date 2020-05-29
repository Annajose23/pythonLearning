numbers = [1,3,1,4,7,6]
first = set(numbers)
print(list(first))

second = {2,3,3,9,9,10}
print(first | second) #union
print(first & second) #intersection
print(first-second) #difference
print(first^second) #symmetric difference, eiither in first or seconf but not in both

# we cannot access through index

if 1 in first:
    print("found")