def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def between_two_sets(arr1, arr2):
    lcm_result = 1
    gcd_result = arr2[0]

    for num in arr1:
        lcm_result = lcm(lcm_result, num)

    for num in arr2[1:]:
        gcd_result = gcd(gcd_result, num)

    count = 0
    multiple = lcm_result

    # while multiple <= gcd_result:
    #     if gcd_result % multiple == 0:
    #         count += 1
    #     multiple += lcm_result
    for i in range(0,gcd_result):
        if gcd_result % lcm_result == 0:
            count +=1
            lcm_result +=lcm_result


    return count

# Example usage:
arr1 = [2, 4]  # take lcm of this  LCM = 4
arr2 = [16, 32, 96]   # take gcd of this    GCD = 16
result = between_two_sets(arr1, arr2)
print(result)



###############     Explanation     ################
 
# Suppose GCD is 16  & LCM is 4  ,,,  then we will do in first step 
# 1) LCM(4) % GCD(16) == 0 ,,,,(True) ,,count=+1 LCM(4)+LCM(4)
# 2) LCM(8) % GCD(16) == 0 ,,,,(True) ,,count+=1 LCM(8)+LCM(4)
# 3) LCM(12) % GCD(16) == 0 ,,,,(False) ,,count+=0 LCM(12)+LCM(4)
# 4) LCM(16) % GCD(16) == 0 ,,,,(True) ,,count+=1 LCM(16)+LCM(4)

# 5) LCM(20) % GCD(16) == 0 ,,,,(FALSE) ,,count+=0 LCM(20)+LCM(4) so stop here





