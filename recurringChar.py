def findRecurringChar(s):
    print(s)
    chars = []
    for element in s:
        if element in chars:
            return element
            break
        else:
            chars.append(element)


print(findRecurringChar("BCDABBA"))