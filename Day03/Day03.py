import re
with open('Day03\Day03.txt', 'r') as file:
    file_contents = file.read()
    s1=[]
    s2=[]
    x = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file_contents)
    for i in x:
        a = i[4:-1]
        z, y = a.split(',')

        s1.append(int(z)*int(y))

    print(sum(s1))


    d = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", file_contents)
    on = True
    for i in d:
        if i == "don't()":
            on = False
        elif i == "do()":
            on = True
        elif on:
            a = i[4:-1]
            z, y = a.split(',')

            s2.append(int(z)*int(y))

    print(sum(s2))




