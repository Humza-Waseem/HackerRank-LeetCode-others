# def eliminateMaximum(dist, speed):
#         count =0
#         if(dist[0] >= 1 and speed[0] == 1 ):
#             count= count +1
#         # else:
#         #     return count
#         t = 0
#         for i in range(1,len(dist)):
#             t = dist[i] / speed[i]

#             # if(dist[i] > 1 and speed[i] > 1):
#             if(t < 0):
#                 # count= count +1
#                 return count
#             # if(dist[i] > 1 and speed[i] == 1):
#             if(t>=1):
#                 count= count +1
#             else:
#                 return count
            
#             # if(dist[i] == 1 and speed[i] >=1):
#             #     return count
#             # if(dist[i] == 1 and speed[i] == 1):
#             #     return count
#         return count 


# dist = [3,2,4]
# speed = [5,3,2]
# val = eliminateMaximum(dist,speed)
# print(val)
