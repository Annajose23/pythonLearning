def fizzBuzz(x):
    if (x%3 == 0) and (x%5 == 0):
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("buzz")
    else:
        print(x)

fizzBuzz(7)
