# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
def migratoryBirds(arr):
    BirdCounts = [0, 0, 0, 0, 0]  # 5 bird types

    for i in arr:
        BirdCounts[i - 1] += 1  #adding 1 to every bird type, if there is a match in the array

    max_count = max(BirdCounts)
    

    for birdType in range(1, 6):
        if BirdCounts[birdType - 1] == max_count:
            return birdType

arr = [1,1,2,2,3]
maxCount = migratoryBirds(arr)
print('Max Count:', maxCount)