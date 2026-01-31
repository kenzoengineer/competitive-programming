# Binary search


def nextGreatestLetter(letters, target):
    l = 0
    r = len(letters)
    while l < r:
        m = (l + r) // 2
        if ord(letters[m]) <= ord(target):
            l = m + 1
        else:
            r = m
    return letters[0] if l >= len(letters) else letters[l]


print(nextGreatestLetter(None, ["c", "f", "j"], "a"))  # "c"
print(nextGreatestLetter(None, ["c", "f", "j"], "c"))  # "c"
print(nextGreatestLetter(None, ["x", "x", "y", "y"], "z"))  # "c"
