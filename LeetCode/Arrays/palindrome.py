# check if an int number is palindrome
def isPalindrome(x):
        if( x == 0) or (x < 10 and x>= 0):
            return True
        if ( x < 0  ) or(x%10 == 0) :
            return False
        
        else:
            half = 0
            while x > half:
                half = (x%10) + (half * 10)
                x = x//10
            if  x == half or x == half// 10:
                return True

        