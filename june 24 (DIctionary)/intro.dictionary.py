# dictionary-
# kay and value ka pair 
# key alaways unique value can be duplicate
# mutable

data={
    "name":"Jatin",
    "rollno":101,
    100:200
}

print(data.get("no","value is not present"))

for i in data.keys():
    print(i)
for i in data.values():
    print(i)

data[1000]=151
for i,j in data.items():
    print(i,j)

    