def printa(a):
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()

def lcs(x, y):
    m = len(x)
    n = len(y)
    arr = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):
                arr[i][j] = 0
            elif(x[i-1] == y[j-1]):
                arr[i][j] = 1 + arr[i-1][j-1]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    printa(arr)
    i = len(arr)-1
    j = len(arr[0])-1
    str = ""
    while(i > 0 and j > 0):
        if(arr[i][j-1] == arr[i][j]):
            j -= 1
        else:
            str = str+ y[j-1]
            i = i - 1
            j = j - 1
    print(str[::-1])


'''
w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
lcs(w1, w2)
'''

lcs('stone', 'longest')
