# 20. Valid Parentheses

class Stack:
    def __init__(self):
        self.top = None


def isValid( s):
    openingBrackets = "{[("
    closingBrackets = ")]}"
    stack = []
    for chr in s:
            if(chr in openingBrackets):
                stack.append(chr)
                print("item appended")
            elif(chr in closingBrackets):
                bracket = stack.pop()
                
               

                
s = "(]"
flag = isValid(s)
print(flag)





