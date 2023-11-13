def is_leap(year):
    leap = False
    
    if(year % 4 == 0  ):
    
          if(year == 2100):
            return False
          else:
           return True
       
    elif(year % 400 == 0 ): 
          if(year == 2100):
            return False
          else:
           return True
    
    elif(year % 100 != 0 ):
        
        leap = False
   
    else:
       leap = False 
    return leap

year = int(input())
print(is_leap(year))