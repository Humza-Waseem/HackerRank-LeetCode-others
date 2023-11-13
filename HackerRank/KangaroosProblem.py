def kangaroo(x1, v1, x2, v2):
    # Write your code here
   
    if  v1 > v2:
        if(x2-x1) % (v1-v2) == 0:
            return"YES"
        else:
            return "NO"
    


def kangaroo(x1, v1, x2, v2):
    # Check if the kangaroos have the same initial location and velocity
    if x1 == x2 and v1 == v2:
        return "YES"
    
    # Check if the kangaroos have the same velocity, but different initial locations
    if v1 == v2:
        return "NO"
    
    # Check if the relative distance between the kangaroos is divisible by the relative velocity
    relative_distance = x2 - x1
    relative_velocity = v1 - v2
    
    if relative_velocity != 0 and relative_distance % relative_velocity == 0 and relative_distance / relative_velocity >= 0:
        return "YES"
    else:
        return "NO"
        

# Example usage:
result = kangaroo(0, 3, 4, 2)
print(result)

        

x1 = 0
v1 = 2
x2 = 5
v2 = 3
print(kangaroo(x1,v1,x2,v2))