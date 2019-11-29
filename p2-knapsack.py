def par(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def knapsack(weight, value, total):
    n = len(value)
    arr = [[0 for x in range(total+1)] for x in range(n)]
    par(arr)

    for i in range(n):
        for j in range(total+1):
            if(j == 0):
                arr[i][j] = 0
            elif(j < weight[i]):
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = max(value[i] + arr[i-1][j-weight[i]], arr[i-1][j])
    par(arr)

    str1 = ""
    i = len(arr)-1
    j = len(arr[0])-1
    while(i >= 0 and j >= 0):
        if(arr[i-1][j] == arr[i][j]):
            i = i-1
        else:
            str1 = str1 + str(weight[i]) + " "
            j = j-weight[i]
            i = i-1
    print("Items: " +str1)


wt = [1,3,4,5]
val = [1,4,5,7]
t = 7
knapsack(wt, val, t)
