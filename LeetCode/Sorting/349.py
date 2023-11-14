def Intersection(nums1,nums2):
        array = []
        for i in range(0,len(nums1)):
            key = nums1[i]
            if (key not in array) and (key in nums2):
              for j in range(0,len(nums2)):
                if(key == nums2[j]):
                    array.append(key)
                    break
                else:
                    continue
        return array

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
val = Intersection(nums1,nums2)
print(val)