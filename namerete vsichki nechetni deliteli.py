str=input("Enter a string: ")
i=0
for i in range(str):
    print(str[i])
    if str[i]=="  ":
        print("i=i+1")
        continue 