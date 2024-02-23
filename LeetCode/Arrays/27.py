

def removeElement( nums, val):
        array = []
        count = 0
        for i in range(0,len(nums)):
            if(nums[i] != val):
                array.append(nums[i])
                count+=1
            else:
                continue
        return count,array

# array = [1, 1,1, 2,2,]

# val = 1
array = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(array,val))



