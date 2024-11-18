# Sort, geometry, heap

def kClosest(points, k):
    # no point in taking the square root, takes a long time
    # max heap would also work!
    def dist(x,y):
        return x**2 + y**2

    points.sort(key=lambda x: dist(x[0],x[1]))
    return points[:k]