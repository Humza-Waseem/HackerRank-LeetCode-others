# def romanToInt(self, s: str) -> int:
#         count = 0
#         roman = {
#             'I': 1,
#             'V': 5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }
#         for i in range(len(s)-1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 count = count - roman[s[i]]
#             else:
#                 count += roman[s[i]] 
#         return count + roman[s[len(s)-1]]  # adding the last character to our result
#         # or 
#         # return count + roman[s[-1]]  # adding the last character to our result


def fib(target):
    first = 0
    second = 0
    count = 0
    