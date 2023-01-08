# Math, Hashing, Geometry

test = [[1,1],[[3,2],[5,3],[4,1],[2,3],[1,4]]]
test = [[1,1],[1,1],[1,1],[1,2]]
def maxPoints(points):
    # "m,b" in y = mx + b
    # if the line is vertical, it will be "a" in x = a
    eqns = dict()
    point_counts = dict()
    res = 0
    if len(points) <= 2:
        return len(points)
    for p in points:
        if f"{p[0],p[1]}" in point_counts:
            point_counts[f"{p[0],p[1]}"] += 1
        else:
            point_counts[f"{p[0],p[1]}"] = 1
    point_unique = list(set(tuple(i) for i in points))
    print(point_unique)
    for x in range(len(point_unique)):
        for i in range(x):
            print(f"{point_unique[x][0]} {point_unique[i][0]}")
            if point_unique[x][0] == point_unique[i][0]:
                if str(point_unique[x][0]) in eqns:
                    eqns[str(point_unique[x][0])] += 1
                    res = max(res, eqns[str(point_unique[x][0])])
                else: 
                    eqns[str(point_unique[x][0])] = 2
                    res = max(res, eqns[str(point_unique[x][0])])
                continue
            m = (point_unique[x][1] - point_unique[i][1]) / (point_unique[x][0] - point_unique[i][0])
            b = point_unique[x][1] - m * point_unique[x][0]
            if f"{m},{b}" in eqns:
                eqns[f"{m},{b}"] += 1
                res = max(res, eqns[f"{m},{b}"])
            else:
                eqns[f"{m},{b}"] = 2
                res = max(res, eqns[f"{m},{b}"])
    print("----------")
    print("LINE [M,B] | FREQUENCY")
    for x in eqns:
        print(x, end="\r\t\t| ")
        print(eqns[x])
    print("POINT | FREQUENCY")
    for x in point_counts:
        print(x, end=" | ")
        print(point_counts[x])
    return res

    
print(maxPoints(test))