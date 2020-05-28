print("hello Anna")

student = True
print(type(student))

x = 10
print(id(x))

x = x +1
print(id(x))

y = [1,2,3,4]
print(id(y))

y.append(5)
print(y)
print(id(y))

course = "python learning"
print(len(course))
print(course[0])
print(course[0:3])
print(id(course))
print(id(course[0:9]))

print("python \"programming") 
print("python \\ progamming")
print("python \nprogramming")

first = "anna"
last = "jose"
full = f"{first} {last}"
print(full)

course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("thp"))
print(course.replace("p", "-"))
print("pyth" in course)
print("python" not in course)

x =10
print(bin(x))
print(hex(x))

print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10//3)
print(10**3)
print(10*3)
print(10%3)

# z = input("x:")

# print(int(z))
# print(bool(z))
# print(float(z))

age = 2

if age >= 18:
    print("adult")
elif age < 18:
    print("minor")
else:
    print("not eligible")

name = ""

if not name:
    print("no name")
else:
    print(name)

myAge = 27

if not age:
    print("no age")
elif(myAge >= 18 and myAge < 60):
    print("eligible")

age = 90
message = "eligible" if age>=18 else "not eligible"
print(message)


for x in "python":
    print(x)

for y in ['a', 'b', 'c', 'd']:
    print(y)

for i in range(0,10,2):
    print(i)

names = ["Anna" , "Able"]

for name in names:
    if name.startswith("A"):
        print("found")
        break
else:
    print("not found")

# guess = 0
# answer = 5
# while answer != guess:
#    guess = int(input("guess : "))


def increment(number, by):
    return number + by

print(increment(3,4))