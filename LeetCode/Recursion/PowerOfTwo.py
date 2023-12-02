# power of 2 function
# def power_of_two(n):
#     if n == 0:
#         return False
#     while n != 1:
#         if n % 2 != 0:    
#             return False
#         n = n // 2
#     return True


def power_of_two(n):
    if n == 0:
        return False

    if n == 1:
        return True
    if n % 2 != 0:    
        return False

    return power_of_two(n // 2)


