def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def shortest(arr):
    t = 0
    n = len(arr)
    while(t < n):
        for x in range(n):
            for y in range(n):
                if x == y:
                    arr[x][y] = 0
                elif x == t or y == t:
                    pass
                else:
                    arr[x][y] = min(arr[x][y], arr[t][y] + arr[x][t])
        t += 1
    printa(arr)

arr = [[0, 2, 99, 1, 8], [6, 0, 3, 2, 99], [99, 99, 0, 4, 99], [99, 99, 2, 0, 3], [3, 99, 99, 99, 0]]
shortest(arr)
