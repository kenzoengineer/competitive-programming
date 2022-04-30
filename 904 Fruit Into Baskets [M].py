# Sliding Window

fruits = [1,2,3,2,2,1]

def totalFruit(fruits):
    left = 0
    m = 0
    d = dict()
    for i in range(len(fruits)):
        if fruits[i] not in d:
            if len(d) >= 2:
                to_delete = ""
                for x in d:
                    if x != fruits[i-1]:
                        to_delete = x
                        left = d[x] + 1                  
                del d[to_delete]
        m = max(i - left + 1,m)
        d[fruits[i]] = i
    return m
print(totalFruit(fruits))