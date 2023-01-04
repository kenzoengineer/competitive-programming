# String, Array. Hash

t_1 = "abba"
t_2 = "dog cat cat dog"
def wordPattern(pattern, s):
    match = dict()
    words = set()
    s = s.split(" ")
    if len(s) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in match:
            match[pattern[i]] = s[i]
            if s[i] in words:
                return False
            words.add(s[i])
        else:
            if s[i] != match[pattern[i]]:
                return False
    return True

print(wordPattern(t_1, t_2))
