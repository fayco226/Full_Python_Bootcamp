string = input("enter a string")

if len(string) > 10:
    print("string too long")
elif len(string) < 10:
    print("string not long enough")
print("first caractere is ", string[0],"\nlast caractere is ", string[-1])
result = ""
for i in string:
    result = result + i
    print(result)
