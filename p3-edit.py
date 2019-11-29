def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def edit(str1, str2):
    m = len(str1)
    n = len(str2)
    arr = [[0 for x in range(n+1)] for y in range(m+1)]
    printa(arr)

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0):
                arr[i][j] = j
            elif(j==0):
                arr[i][j] = i
            elif(str1[i-1] == str2[j-1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = 1+min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
    printa(arr)
    print("Edit distance: " +str(arr[m][n]))

edit("abcdef", "azced")
