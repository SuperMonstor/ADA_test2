def subseq(arr):
    n = len(arr)
    temp = [1 for x in range(n)]

    for i in range(1, n):
        for j in range(i):
            if(arr[j] < arr[i] and temp[i] < temp[j] + 1):
                temp[i] = temp[j]+1
    print(temp)
    print(max(temp))

subseq([50, 3, 10, 7, 40, 80])
