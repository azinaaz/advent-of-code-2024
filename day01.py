file = open("01data.txt" , "r")
data = file.readlines()
x=[]
y=[]
for line in data:
    a, b =line.split()
    x.append(int(a))
    y.append(int(b))
x.sort()
y.sort()

s=0
for i in range(0, len(x)):
    s += (abs(x[i] - y[i]))
print(s)

w=[]
for i in range(0, len(x)):
    w.append(x[i] * y.count(x[i]))

print(sum(w))
     



    
    
    