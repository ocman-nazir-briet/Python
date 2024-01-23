"""
Remember in List Index Starts from 0 
"""

# Search in Lists

list = [10,5,9,4,8,3,7,2,6,1, "Ocman"]
print(list)

if 10 in list:
    print("10 Found")


if 100 not in list:
    print("100 Not Found")

for i in range(len(list)):
    if list[i] == 2:
        print("2 Found Inside Loop at Index", i)
    else:
        pass

if "ocman" in list:
    print("ocman Found")

if "ocman" not in list:
    print("ocman not Found")

if "Ocman" in list:
    print("Ocman Found")

if "Ocman" not in list:
    print("Ocman Not Found")

for i in range(len(list)):
    if list[i] == "Ocman":
        print("Ocman Founf at Index", i)


# Search in String
my_str = "i am a software engineer"
if "soft" in my_str:
    print("sub-string Found")
else:
    print("sub-string not Found")