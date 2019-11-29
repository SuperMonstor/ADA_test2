def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def minimum(coins, total):
    n = len(coins)
    arr = [[0 for x in range(total+1)] for x in range(len(coins))]
    printa(arr)
    for i in range(n):
        for j in range(total+1):
            if(i == 0):
                arr[i][j] = j
            elif(j < coins[i]):
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = min(1+arr[i][j-coins[i]], arr[i-1][j])
    printa(arr)

    i = len(arr)-1
    j = len(arr[0])-1
    str1 = ""
    while(i > 0 and j > 0):
        if(arr[i][j] == arr[i-1][j]):
            i = i-1
        else:
            j = j - coins[i]
            str1 = str1 + str(total-coins[i]) +" "
    print(str1)

coins = [1, 5, 6, 8]
total = 11
minimum(coins, total)
