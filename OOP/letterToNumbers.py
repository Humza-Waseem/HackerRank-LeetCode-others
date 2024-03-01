def main(st):
    numbersDict = { "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000}

    strings = st.split(" ")
    length = len(strings)
    if(length == 1):
        return numbersDict[strings[0]]
    elif(length == 2 ):
        return numbersDict[strings[0]] + numbersDict[strings[1]]
    elif(length == 3 and strings[1] == "hundred"):
        return numbersDict[strings[0]] *  numbersDict[strings[1]]  +   numbersDict[strings[2]]
    
    
    return None
    




if __name__ == "__main__":
    st = input("enter the string:")
    answer = main(st)
    print(answer)