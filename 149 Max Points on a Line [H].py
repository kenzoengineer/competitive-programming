# Math, Hashing, Geometry

# the leetcode solution is really smart take a look at it
# you calculate slopes at every point

test = [[54,153],[1,3],[0,-72],[-3,3],[12,-22],[-60,-322],[0,-5],[-5,1],[5,5],[36,78],[3,-4],[5,0],[0,4],[-30,-197],[-5,0],[60,178],[0,0],[30,53],[24,28],[4,5],[2,-2],[-18,-147],[-24,-172],[-36,-222],[-42,-247],[2,3],[-12,-122],[-54,-297],[6,-47],[-5,3],[-48,-272],[-4,-2],[3,-2],[0,2],[48,128],[4,3],[2,4]]

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def maxPoints(points):
    # "m,b" in y = mx + b
    # if the line is vertical, it will be "a" in x = a
    eqns = dict()
    point_counts = dict()
    res = 0
    if len(points) <= 2:
        return len(points)
    for p in points:
        if f"{p[0]},{p[1]}" in point_counts:
            point_counts[f"{p[0]},{p[1]}"] += 1
        else:
            point_counts[f"{p[0]},{p[1]}"] = 1
    point_unique = list(set(tuple(i) for i in points))
    for x in range(len(point_unique)):
        done_set = set()
        for i in range(x):
            if point_unique[x][0] == point_unique[i][0]:
                if str(point_unique[x][0]) in eqns:
                    if str(point_unique[x][0]) not in done_set:
                        eqns[str(point_unique[x][0])] += 1
                        done_set.add(str(point_unique[x][0]))
                        res = max(res, eqns[str(point_unique[x][0])])
                else: 
                    eqns[str(point_unique[x][0])] = 2
                    done_set.add(str(point_unique[x][0]))
                    res = max(res, eqns[str(point_unique[x][0])])
                continue
            m = (point_unique[x][1] - point_unique[i][1]) / (point_unique[x][0] - point_unique[i][0])
            if (m == -0.0):
                m = 0.0
            b = point_unique[x][1] - m * point_unique[x][0]
            b = float(truncate(b, 10))
            b = round(b,9)
            if f"{m},{b}" in eqns:
                if f"{m},{b}" not in done_set:
                    done_set.add(f"{m},{b}")
                    eqns[f"{m},{b}"] += 1
                    res = max(res, eqns[f"{m},{b}"])
            else:
                eqns[f"{m},{b}"] = 2
                done_set.add(f"{m},{b}")
                res = max(res, eqns[f"{m},{b}"])

    for p in point_counts:
        x = p.split(",")[0]
        y = p.split(",")[1]
        if point_counts[p] > 1:
            for eqn in eqns:
                # vertical
                if eqn.find(",") == -1 and int(eqn[0]) == int(x):
                    eqns[eqn] += point_counts[p] - 1
                    res = max(res,eqns[eqn])
                elif eqn.find(",") != -1:
                    mb = eqn.split(",")
                    # if y = mx + b
                    if int(y) == (float(mb[0]) * int(x) + float(mb[1])):
                        eqns[eqn] += point_counts[p] - 1
                        res = max(res,eqns[eqn])
    if res == 0:
        for x in point_counts:
            res = point_counts[x]
    return res
    
print(maxPoints(test))