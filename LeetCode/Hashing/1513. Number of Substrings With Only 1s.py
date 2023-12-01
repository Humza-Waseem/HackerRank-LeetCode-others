# //1513. Number of Substrings With Only 1s



class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if(i<j):  # if i<j, then only we will proceed further, otherwise not.
                    if(s[i:j] == '1'*len(s[i:j])):  # by  '1'*len(s[i:j]) expression, we will create a string of length len(s[i:j]) that consists only of the character '1'. If the two strings are equal, then the current substring consists only of the character '1'. 
                        
                        # print("i = ",i)
                        # print("j = ",j)
                        # print("range of values = ",s[i:j])
                        count+=1
                        # print("count = ",count)
        return count

s = "0110111"
sol = Solution()
val = sol.numSub(s)
print(val)
# print(s[0:3])


###########     Explanation     ###########:

# we have to find the number of substrings that consist only of the character '1'.

# Example 1:
# Input: s = "0110111"
# Output: 9

# 1) we will see if the range of values of s[i:j] is contain only the '1's 
# 2) if it the range only contain '1's then we will increment the count by 1.
# 3) if there is a range in which there is any '0' then we will not increment the count.

#  The range should only contain the '1's. If there is any '0' in the range then we will not increment the count.




##############    Solution2   ##############

def numSub(self, s: str) -> int:
        count = 0  # variable to store the total count of substrings
        consecutive_ones = 0  # variable to store the length of the current consecutive sequence of '1's
        mod_value = 10**9 + 7  # to handle large numbers in Python  (1000000007)

        # s = "0110111"
        for char in s:
            if char == '1':
                consecutive_ones += 1
                count = (count + consecutive_ones) % mod_value    # eg (1) mod 1000000007 = 1 , (2) mod 1000000007 = 2  (3) mod 1000000007 = 3  ,  (4) mod 1000000007 = 4  ,  (5) mod 1000000007 = 5  ,  (6) mod 1000000007 = 6  ,(7) mod 1000000007 = 7
            else:
                consecutive_ones = 0

        return count
