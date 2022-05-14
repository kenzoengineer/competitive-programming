# Two Pointer
t_s = "ab##"
t_t = "c#d#"

# Didn't finish this, have to push the other pointer back depending on how much the pointer is backspaced
# Easy if you just use a stack, harder if you use two pointer

def backspaceCompare(s, t):
    sPointer = len(s) - 1
    tPointer = len(s) - 1
    sBack = 0 
    tBack = 0
    while (sPointer >= 0 and tPointer >= 0):
        while (s[sPointer] == "#"):
            sBack += 1
            sPointer -= 1
        sPointer -= sBack
        while (t[tPointer] == "#"):
            tBack += 1
            tPointer -= 1
        tPointer -= tBack
        if (s[sPointer] != t[tPointer]):
            return False
        sBack = 0
        tBack = 0
        sPointer -= 1
        tPointer -= 1
    return (sPointer < 0 and tPointer < 0)
print(backspaceCompare(t_s,t_t))
