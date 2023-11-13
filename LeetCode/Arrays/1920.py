# Build Array from Permutation

def BuildArray(array):
    ans = []
    index = 0
    if(len(array) != None):
        for i in range(0 , len(array)):
            ans.append(array[array[i]] )
        return ans
    else:
           return None

array = [0,2,1,5,3,4]
ans = BuildArray(array)
print(ans)


