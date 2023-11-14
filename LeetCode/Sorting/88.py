def MergeTwoArrays(arr1,arr2, m , n):
    newArray = []
    for i in range( 0 , m):
        newArray.append( arr1[i])
    for i in range(0 , n):
        newArray.append( arr2[i] )

    return newArray


def merge_sort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, it is already sorted.
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves back together
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left and right lists (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# array1 = [1,2,3,0,0,0]
# array2 = [2,5,6]


# array = MergeTwoArrays(array1,array2,3,3)
# sortedArray = merge_sort(array)
# print(sortedArray)

    
