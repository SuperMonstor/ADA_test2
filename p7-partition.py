def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def findarrition(mat):
    n = len(mat)
    if(n%2 != 0):
        return False
    arr = [[None for x in range(n+1)] for y in range(n)]
    printa(arr)
    for x in range(n+1):
        for y in range(n):
            if(x == 0):
                arr[x][y] = True
            elif(y==0 and x != 0):
                arr[x][y] = False
            elif x >= mat[y - 1]:
                arr[x][y] = (arr[x][y] or arr[x - mat[y - 1]][y - 1])
            else:
                arr[x][y] = arr[x][y - 1]


    printa(arr)


arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
findarrition(arr)
