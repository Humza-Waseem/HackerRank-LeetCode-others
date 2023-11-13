#####     EXPLANATION   #####

# WE Have :
#       "s" as the starting of the house 
#       "t" as the ending of the house

#        "a"  is the Location of Apple Tree which is left to the "s"
#        "b"  is the location of Orange tree which is to the right of "t"

#      A      s-------t     B

def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApples = 0
    countOranges = 0

    for appleDistance in apples:
        appleLandingPosition = a + appleDistance
        if(appleLandingPosition  <= t  and appleLandingPosition >= s):
            countApples = countApples + 1

    for orangeDistance in oranges:
        orangeLandingPosition = b  + orangeDistance
        if(orangeLandingPosition  <= t  and orangeLandingPosition >= s):
            countOranges = countOranges + 1
    print(countApples)
    print(countOranges)



s = 7
t = 11
a  = 5
b = 15
apples = [-2,2,1]
oranges = [5,-6]
countApplesAndOranges(s,t,a,b,apples,oranges)
    
