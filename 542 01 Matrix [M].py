# Array, BFS

def updateMatrix(mat):
    # start at each 0 and BFS from each point

    def inRange(mat, i, j):
        if i >= 0 and j >= 0 and i < len(mat) and j < len(mat[0]):
            return True
        return False

    q = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                q.append((i,j,0))
    res = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    print(q)
    while len(q):
        coord = q.pop(0)
        if res[coord[0]][coord[1]] != -1:
            continue
        res[coord[0]][coord[1]] = coord[2]
        if inRange(mat, coord[0]-1, coord[1]):
            q.append((coord[0]-1,coord[1],coord[2]+1))
        if inRange(mat, coord[0]+1, coord[1]):
            q.append((coord[0]+1,coord[1],coord[2]+1))
        if inRange(mat, coord[0], coord[1]-1):
            q.append((coord[0],coord[1]-1,coord[2]+1))
        if inRange(mat, coord[0], coord[1]+1):
            q.append((coord[0],coord[1]+1,coord[2]+1))
    return res