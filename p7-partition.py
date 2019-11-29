def findPartition(arr, n):
    total = 0
    i, j = 0, 0
    total = sum(arr)
    part = [[None for x in range(n+1)] for y in range(total // 2 + 1)]
    print(part)
    if total % 2 != 0:
        return False

    for i in range(total // 2 + 1):
        for j in range(n + 1):
            if(i == 0):
                part[i][j] = True
            elif(j == 0 and i != 0):
                part[i][j] = False
            elif i >= arr[j - 1]:
                    part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
            else:
                    part[i][j] = part[i][j - 1]
    print(part[total // 2][n])

arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
findPartition(arr, n)
