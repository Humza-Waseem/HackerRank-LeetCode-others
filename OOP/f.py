def main():
    # arr=[]
    # for i in range(3):
    #     arr.append(int(input()))
    # if (arr[0]==arr[1] and arr[1]==arr[2]):
    #     print("equilateral")
    # elif(arr[0]==arr[1] or arr[1]==arr[2] or arr[2]==arr[0]):
    #     print("isosceles")
    # else:
    #     print("scalene")

    row = 3
    col = 3
    matrix = []
    count = 0
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(int(input()))
    for i in range(row):
        for j in range(col):
            if (matrix[i][j+i] == 1):
                count +=1
            # elif (matrix[i][j+] == 1):
            #     count +=1
            elif (matrix[i][j] == 1):
                count +=1

    #function to convert one,two upto 1000 to 1,2,...,1000

    
    
            
            
        
            # print(matrix[i][j], end=" ")
    print(count)
    

if __name__ == "__main__":
    main()

