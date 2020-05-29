letters = ["a", "b", "c"]
# lists
matrix = [[0,1],[2,3]]

zeros = [0] * 5

combined = zeros + letters
# print(combined)

numbers = list(range(20))
# print(numbers)

chars = list("hello world")

# print(list("hello world"))

numbers = list(range(20))
# reverse an array
print(numbers[::-1]) 

numbers = [1,2,3,4,5,6,7,8,9]
# unpacking
first,second,*others = numbers
# print(first)
# print(others)
# when we prefix a parameter with a * python will get all this arbitory arguments packed in a list 

# looping over lists

letters = ['a','b','c']

for index, letter in enumerate(letters):
    print(index,letter)

# each iteration it will retun a tuple

# Adding and removing items in a list
alphabets = ['a','b','c','d']
# Add
alphabets.append('e')
alphabets.insert(0,'z')

# delete
alphabets.pop(2)
alphabets.remove('a')
del alphabets[0:3]
letters.clear()

#print(alphabets)

#find

alphabets = ['a','b','c','d']
#find index of object in a list
#print(alphabets.index('b'))

#if not in list
#print(alphabets.count('e'))

if "e" in alphabets:
    print(alphabets.index("e"))

#sorting

numbers = [3,7,90,43,12,55]
print(sorted(numbers))
print(sorted(numbers, reverse=True)) #reverse

#sorting complex items

items = [
    ("apple", 10),
    ("banana", 20),
    ("pineapple", 40),
    ("water melon", 5)
]

# def sort_item(item):
#     return item[1]

# items = items.sort(key=sort_item)
# print(items)

items.sort(key=lambda item: item[1])
#print(items)

#MAP FUNCTION
prices = list(map(lambda item: item[1], items))
print(prices)

#FILTER FUNCTION
filtered = list(filter(lambda item: item[1] > 10, items))
print(filtered)

#LIST COMPREHENSION
#MAP
items = [item[1] for item in items]
print(items)
#FILTER
#filtered = [item for item in items if item[1]>=10]
#print(filtered)

#ZIP FUNCTION - MAkE TUPLE - MULTIPLE LIST COmbine

list1 = [1,2,3,4]
list2 = [10,20,30,40]

print(list(zip(list1,list2)))

print(list(zip("abcd", list1, list2)))




