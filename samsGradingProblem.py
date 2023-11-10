def gradingStudents(grades):
    for i in range(0,len(grades)):
        modulo = grades[i] % 10
        if(grades[i] + 3 > 40):
          if(modulo < 5  ):
            sub = 5 - modulo 
            if(sub >= 3 ):
                continue
            elif(sub<3):
                grades[i] = grades[i] +  sub
          elif(modulo > 5):
            sub = 10 - modulo
            if(sub >= 3 ):
                continue
            elif(sub<3):
                grades[i] = grades[i] +  sub
        else:
            continue
    return grades
 
                

grades = [73,67,38,33]    # test case 1
# grades = [54,37,38,36,99]
print(len(grades))
array = gradingStudents(grades)
print(array)