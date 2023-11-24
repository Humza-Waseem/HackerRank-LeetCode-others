def divisibleSumPairs(n, k, ar):
    
    j = 1
    count = 0

    for i in range(0,n):
        for j in range(i+1,n):
            if(i < j):
               if((ar[i] + ar[j]) % k == 0):
                   count+=1
    return count
            

ar = [1, 3, 2, 6, 1, 2]
k = 3
val  = divisibleSumPairs(6, k, ar)
print(val)
