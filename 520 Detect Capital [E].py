# String

test = "Leetcode"
def detectCapitalUse(word):
    return word.upper() == word or word.lower() == word or word[0].upper() + word[1:].lower() == word

print(detectCapitalUse(test))
