#########################LONGEST COMMON PREFIX#######################

#WE USED VERTICAL SCANNING APPROACH FOR THIS PROBLEM WHERE WE SELECT A WORD AND COMPARE ITS CHARACTERS ONE BY ONE WITH ALL THE OTHER WORD'S CHARACTERS IN THE LIST
def longestCommonPrefix(strs):
     if not strs:    # if there are no strings in the list then return empty
        return ""
     firstword = strs[0] 
     for i in range(len(firstword)):
        for word in strs[1:]:  
            if (i == len(word) or word[i] != firstword[i]):  # if the index is greater than the length of the word or the character at the index is not equal to the character at the index of the first word then return the first word upto the index 
                return firstword[0:i]
     return firstword        
strs = ["flower","floe","flight"]
print(longestCommonPrefix(strs))