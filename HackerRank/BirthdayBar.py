
def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(0,len(array)):
        if sum(array[i:i+m]) == d:   #  array[i:i+m] is a slice of array from i to i+m means,, in the first iteration 
            # arr[0: 0+ m=2]  sum will be evaluated ,,, then second iteration,,, arr[1,1+m= 3] sum will be evaluated
            count += 1
    return count
    
array = [2,2,1,3,2]

d = 4
m= 2

result = birthday(array,d,m)
print(result)


###############     PROBLEM STATEMENT    ###################
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# # The length of the segment matches Ron's birth month, and,
# # The sum of the integers on the squares is equal to his birth day.
# # # Determine how many ways she can divide the chocolate.


#$$$$$$$$$$$$$$$$$$   EXPLANATION  $$$$$$$$$$$$$$$$$$$$

# WE WILL Sum arr[i] upto the number of m(birth month)   and try to make the the sum equal to the birthday
# if the sum = birthday then we will increment the count variable
