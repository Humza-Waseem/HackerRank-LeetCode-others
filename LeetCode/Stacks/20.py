# 20. Valid Parentheses

# class Stack:
#     def __init__(self):
#         self.top = None


# def isValid( s):
#     openingBrackets = "{[("
#     closingBrackets = ")]}"
#     stack = []
#     for chr in s:
#             if(chr in openingBrackets):
#                 stack.append(chr)
#                 print("item appended")
#             elif(chr in closingBrackets):
#                 bracket = stack.pop()
                

def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

               

                
s = "()"
flag = isValid(s)
print(flag)





