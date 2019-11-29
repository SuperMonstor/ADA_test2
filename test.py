'''
    testing some scripts
'''
def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    arr =[[0 for x in range(n+1)] for y in range(m+1)]
    for x in range(m+1):
        for y in range(n+1):
            if(x==0 or y==0):
                arr[x][y] = 0
            elif(str1[x-1] == str2[y-1]):
                arr[x][y] = 1 + arr[x-1][y-1]
            else:
                arr[x][y] = max(arr[x-1][y], arr[x][y-1])
    printa(arr)
    str3 = ""
    while(m > 0 and n > 0):
        if(arr[m][n-1] == arr[m][n]):
            n = n -1
        else:
            str3 = str3 + str2[n-1] +" "
            m = m -1
            n = n -1
    print(str3[::-1])

def knapsack(weight, value, total):
    n = len(weight)
    arr = [[0 for x in range(total+1)] for x in range(n)]
    for x in range(n):
        for y in range(total+1):
            if(y == 0):
                arr[x][y] = 0
            elif(weight[x] > y):
                arr[x][y] = arr[x-1][y]
            else:
                arr[x][y] = max(value[x] + arr[x-1][y-weight[x]], arr[x-1][y])
    printa(arr)
    f = ""
    n = len(arr)-1
    total = len(arr[0])-1
    while(n >= 0 and total >= 0):
        if(arr[n-1][total] == arr[n][total]):
            n = n-1
        else:
            f = f + str(weight[n]) +" "
            total = total - weight[n]
            n = n - 1
    print(f)

def minedit(str1, str2):
    m = len(str1)
    n = len(str2)
    arr = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0):
                arr[i][j] = j
            elif(j == 0):
                arr[i][j] = i
            elif(str1[i-1] == str2[j-1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = 1+min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
    printa(arr)
    print("Edit distance: " +str(arr[m][n]))

minedit("abcdef", "azced")
