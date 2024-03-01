class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

def sweetestIcecream(ice_cream_list):
    flavor_sweetness = {
        'Plain': 0,
        'Vanilla': 5,
        'ChocolateChip': 5,
        'Strawberry': 10,
        'Chocolate': 10
    }

    max_sweetness = []
    # i = 0
    for ice_cream in ice_cream_list:
        sweetness = flavor_sweetness[ice_cream.flavor] + ice_cream.sprinkles
        max_sweetness.append(sweetness) 
        # i += 1
    

    return max(max_sweetness)

# Example usage:
# ice1 = IceCream('Plain', 3)
# ice2 = IceCream('Vanilla', 2)
# ice3 = IceCream('ChocolateChip', 5)
# ice4 = IceCream('Strawberry', 8)
# ice5 = IceCream('Chocolate', 2)

# result1 = sweetestIcecream([ice1, ice2, ice3, ice4, ice5])
# result2 = sweetestIcecream([ice3, ice1])
# result3 = sweetestIcecream([ice3, ice5])

# print(result1)  # Output: 23
# print(result2)  # Output: 23
# print(result3)  # Output: 17




def fib(n):
    first = 1 
    second = 1
    if  n== 0:
        return first
    if n == 1:
        return second
    while n > 2 :
        first, second = second, first + second
        n -= 1
    return second

# print(fib(0))  # Output: 1
# print(fib(2))  # Output: 1
# print(fib(3))  # Output: 2
# print(fib(4))  
# print(fib(5))  


