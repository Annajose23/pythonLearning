point = {"x" : 1, "y" : 2} #dictionary is "key" : value

point = dict(x=1,y=2) #way to define dictionary
print(point)

point["x"] = 10
point["z"] = 20 #assigning values or changing values of dictionary
print(point)

if "a" in point:
    print(point["a"]) #checking whether value exist or not
if not "a" in point:
    point["a"] = 30 #inserting value if not exist
print(point)

print(point.get("a",0)) #hey check if there is key called a, if not return 0, if yes return value 

del point["x"] #delete key "x"
print(point)

#iterating
for key in point:
    print(key, point[key])

#DICTIONARY COMPREHENSIONS
