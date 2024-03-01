def maximumOddBinaryNumber(binary_string):
         ones_array = []
         zeros_array = []

         for n in binary_string:
             if n == '1':
                 ones_array.append(1)
             elif n == '0':
                 zeros_array.append(0)
             else:
                 return None

         if(ones_array == []):
            return zeros_array
         
         ones_array.extend(zeros_array)
         newOne= ones_array.pop(0)
         ones_array.insert(len(ones_array),newOne)
         return ones_array
         
        
         
if __name__ == "__main__":
    binary_string = str("010")  
    answer = maximumOddBinaryNumber(binary_string)
    print(answer)




