arr = [7 ,69, 2 ,221 ,8974]
sum1  = 0
sum2 = 0
j = 0
arr.sort()

# print(len(arr))
for i in range(1,len(arr) ):
    sum1 = sum1 + arr[i]
for i in range(0,len(arr)-1):
    sum2 = sum2 + arr[i]
print(sum2," ",sum1)


   