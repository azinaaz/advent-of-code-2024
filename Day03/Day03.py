import re
with open('Day03\Day03.txt', 'r') as file:
    file_contents = file.read()
    s=[]
    x = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file_contents)
    for i in x:
        a = i[4:-1]
        z, y = a.split(',')

        s.append(int(z)*int(y))

    print(sum(s))


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

            s.append(int(z)*int(y))

    print(sum(s))




