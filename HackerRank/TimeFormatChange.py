def timeConversion(s): 
        hour=s[0:2] 
        if s[-2].upper()=="P": 
            if (hour!="12"): 
                h=int(hour) 
                h+=12 
                return str(h)+s[2:8] 
            else: return s[:8]
        elif s[-2].upper()=="A":
             if hour=="12":
                hour="00"
                return hour+s[2:8]
             else:
                return s[:8]  
#input 
s = input("Enter time zone")
hours = ""
# hour=s[0:2] 
# hour = s[:8]
# print("hours:",hour)


string= timeConversion(s)

print("Converted TIme:",string)