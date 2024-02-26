# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement( nums, val):
        array = []
        count = 0
        for i in range(0,len(nums)):
            if(nums[i] != val):
                array.append(nums[i])
                count=count + 1
            else:
                continue
        print(count)
        print("nums = ",nums)

# array = [1, 1,1, 2,2,]

# val = 1
array = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(array,val))



