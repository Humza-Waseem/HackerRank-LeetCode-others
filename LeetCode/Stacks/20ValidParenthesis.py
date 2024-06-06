# 20. Valid Parentheses

def isValid(s):
     stack = []
     output = False  # Initialize output to False
    
     if s is None:
        return True
    
     for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
            output = False  # Reset output whenever we push an opening parenthesis
        else:
            if not stack:
                return False
            if char == ')' and stack.pop() == '(':
                output = True
                continue
            elif char == '}' and stack.pop() == '{':
                output = True
                continue
            elif char == ']' and stack.pop() == '[':
                output = True
                continue
            else:
                return False
    # CHECKING IF THE STACK IS NOT EMPTY THEN WE WILL RETURN FALSE
     if stack:
        return False
    
     return output

##INPUT HERE
s = "([]"
flag = isValid(s)
print(flag)


###################################   CHATGPT   ########################################
# def isValid(self, s: str) -> bool:
#      stack = []
#      matching_parentheses = {')': '(', '}': '{', ']': '['}
#                             #key  value
#      for char in s:
#         if char in matching_parentheses.values():
#             stack.append(char)
#         elif char in matching_parentheses.keys():
#             if stack == [] or matching_parentheses[char] != stack.pop():
#                 return False
#         else:
#             # If the character is not a parenthesis, we can ignore it
#             continue
    
#      return stack == []  

                





