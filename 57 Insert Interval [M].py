# Array, Binary search

t_1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
t_2 = [4,8]
def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    l = 0
    r = len(intervals) - 1
    m = 0
    ans = len(intervals)
    while l <= r:
        m = (l + r) // 2
        if intervals[m][0] > newInterval[0]:
            ans = m
            r = m - 1
        else:
            l = m + 1 
    intervals.insert(ans, newInterval)
    ans = max(ans,1)

    while ans < len(intervals):
        if intervals[ans - 1][1] >= intervals[ans][0]:
            intervals[ans - 1][1] = max(intervals[ans - 1][1], intervals[ans][1])
            intervals.pop(ans)
        else:
            ans += 1
    return intervals

print(insert(t_1, t_2))