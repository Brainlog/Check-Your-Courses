import json
file_path = "data.json"  

with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    
user_input = input("Kerbores: ")

courses = data[user_input]
sems = set()
done = {}

for course in courses:
    if not course[0:4].isdigit():
        try:
            done['2101'].add(course[0:6])
        except:
            temp = set()
            temp.add(course[0:6])
            done['2101'] = temp
    else:
        try:
            done[course[0:4]].add(course[5:11])
        except:
            temp = set()
            temp.add(course[5:11])
            done[course[0:4]] = temp

temp = set()
failed = set()

done = dict(sorted(done.items()))

for key,value in done.items():
    print(f"\n{key}")
    for val in value:
        print(val)
        if val in temp:
            failed.add(val)
        temp.add(val)


if len(failed) > 0:
    print("\nFailed")
    for fail in failed:
        print(fail)
