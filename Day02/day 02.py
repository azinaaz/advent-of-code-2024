file = open("Day02.txt" , "r")
reports = file.readlines()
report = []
for line in reports:
    level =line.split()
    safe1=[]
    safe2=[]
    for i in range(len(level)-1):
        if all(1 <= (level[i]) - (level[i+1]) <= 3) or all(-3 <= (level[i]) - int(level[i+1]) <= -1):           
            safe1.append(0)
        else:
            safe1.append(1)
        
    if sum(safe1) == 0:
        report.append(1)

print(report)


#     for i in range(len(level)-1):
#         if 1 <= int(level[i]) - int(level[i+1]) <= 3:            
#             safe1.append(0)
#         else:
#             level[:i] + level[i+1:]

#         if -3 <= int(level[i]) - int(level[i+1]) <= -1:
#             safe2.append(0)
#         else: 
#             level[:i] + level[i+1:]

#     if sum(safe1) == 0 or sum(safe2)==0:
#         report.append(1)
# print(len(report))





            
         


    