
###input 
s = "HamzaWaseemSheikh."
name= s[0:5]
print("name s[0:5]:",name)

name1 = s[-2]
print("name1 s[-2] : ",name1)

name1 = s[0:-1]
print("name s[0:-1] : ",name1)

name1 = s[0:11]
print("name1 s[0:11] : ",name1)


####### Reversing the String
string = ""
for i in range(len(s)-1,-1,-1):
    if(i>=0):
      string  = string + s[i]

print(string)





