def bigSorting(unsorted):
    # Write your code here
    for i in range(0,len(unsorted)):
        for j in range(0,(len(unsorted)-1)-i):
            if unsorted[j] > unsorted[j+1]:
                # temp = unsorted[j]
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
    return unsorted

# array = [12303479849857341718340192371,3084193741082938,3084193741082937,200,111,100,2,1]
array = [6,
31415926535897932384626433832795,
1,
3,
10,
3,
5]
sorted = bigSorting(array)
for i in range(len(sorted)):
    print(sorted[i])
# print(sorted)



