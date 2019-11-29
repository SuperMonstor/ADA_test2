def findMinrange(arr):
    n = len(arr)
    k = len(arr[0])
    ptr = [0]*n
    minel, maxel, frange = 0,0,0
    minval, maxval, rangeval = 999, -999, 999
    print(ptr)
    while(True):
         minval, maxval = 999, -999
         mindex= -1
         flag = 0

         for i in range(n):
            if(ptr[i] == k):
                flag = 1
                break
            if(arr[i][ptr[i]] < minval):
                minval = arr[i][ptr[i]]
                mindex = i
            if(arr[i][ptr[i]] > maxval):
                maxval = arr[i][ptr[i]]

         if(flag == 1):
             break

         ptr[mindex] += 1
         if((maxval-minval) < rangeval):
            minel = minval
            maxel = maxval
            rangeval = maxval-minval

    print(minel)
    print(maxel)
    print(maxel-minel)



arr= [
    [4, 7],
    [1, 2],
    [20, 40]
    ]

findMinrange(arr)
