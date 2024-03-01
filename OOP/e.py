# to print the consecutive 1s in a 2d array
def main():
     row = int(input())
     cols = int(input())
     arr = []
     for i in range(row):
            arr.append([])
            for j in range(cols):
                arr[i].append(int(input()))
     count = 0
     for i in range(row):
            for j in range(cols):
                if (arr[i][j] == 1):
                    count +=1
                    
                
    #  print(count)
     print(arr)
     return count

     

    

if __name__ == "__main__":
    coyunt = main()
    print(coyunt)

    
