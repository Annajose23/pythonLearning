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

print(alphabets)

