def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    highestCount = 0
    lowestCount = 0
    
    for i in range(1, len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            highestCount += 1
        elif scores[i] < lowest:
            lowest = scores[i]
            lowestCount += 1
            
    return [highestCount, lowestCount]
