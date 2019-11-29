def subseq(arr):
    n = len(arr)
    temp = [1 for x in range(n)]

    for i in range(1, n):
        for j in range(i):
            if(arr[j] < arr[i] and temp[j] < temp[i] + 1):
                temp[i] = temp[j]+1
    print(temp)
    print(max(temp))

subseq([3,4,-1,0,6,2,3])
