from collections import Counter

def checkMagazine(magazine, note):
    if not Counter(note) - Counter(magazine):
        return "Yes"
    return "No"


print(checkMagazine("two times three is not four", "two times two is four"))