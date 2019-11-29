'''
    testing some scripts
'''
def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def findPartition(arr, n):
    total = sum(arr)

    if total % 2 != 0:
        return False

    part = [[ None for i in range(n + 1)]
                   for j in range(total // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # intialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, total // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, total // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    print(part)
    return part[total // 2][n]

# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
if findPartition(arr, n) == True:
    print("Can be divided into two",
             "subsets of equal total")
else:
    print("Can not be divided into ",
          "two subsets of equal total")
