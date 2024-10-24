import json

file_path = "data.json"  

with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    
user_input = input("Kerbores: ")
data1 = data[user_input]
a=1
b=1
c=1
d=1
e=1
f=1
s = [set({}), set({}), set({}), set({}), set({}), set({})]

for i in range(0, len(data1)):
    if(data1[i][0:4] == '2102'):
        if(a==1):
            print("2102 4th SEM")
            a=0
        print(data1[i][5:])
        s[0].add(data1[i][5:])
    if(data1[i][0:4] == '2201'):  
        if(b==1):
            print("\n2201 5th SEM")
            b=0      
        print(data1[i][5:])
        s[1].add(data1[i][5:])
    if(data1[i][0:4] == '2202'):
        if(c==1):
            print("\n2202 6th SEM")
            c=0
        print(data1[i][5:])
        s[2].add(data1[i][5:])
    if(data1[i][0:4] == '2301'):
        if(d==1):
            print("\n2301 7th SEM")
            d=0
        print(data1[i][5:])
        s[3].add(data1[i][5:])
    if(data1[i][0:4] == '2302'):
        if(e==1):
            print("\n2302 8th SEM")
            e=0
        print(data1[i][5:])
        s[4].add(data1[i][5:])
    if(data1[i][0:4] == '2401'):
        if(f==1):
            print("\n2401 9th SEM")
            f=0
        print(data1[i][5:])
        s[5].add(data1[i][5:])
        

set_fail = set({})

for i in range(0, 6):
    for j in range(i+1, 6):
        set_fail = set_fail.union(s[i].intersection(s[j]))
    
print("\nFailed in:")
for i in set_fail:
    print(i)