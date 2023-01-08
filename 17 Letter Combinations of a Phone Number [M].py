# Backtracking, Array

test ="23"
def letterCombinations(digits):
    letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    res = []
    if len(digits) == 0:
        return []
    def bt(word, index):
        if index >= len(digits):
            res.append(word)
            return
        for letter in letters[int(digits[index])]:
            word += letter
            bt(word, index + 1)
            word = word[:-1]
    bt("", 0)
    return res
print(letterCombinations(test))