# Sorting
t_intervals = [[1,3],[2,6],[8,10],[15,18]]
def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = [intervals.pop(0)]
    while len(intervals) > 0:
        res.append(intervals.pop(0))
        if res[-2][1] >= res[-1][0]:
            res[-2][1] = max(res[-1][1],res[-2][1])
            res.pop(-1)
    return res
print(merge(t_intervals))