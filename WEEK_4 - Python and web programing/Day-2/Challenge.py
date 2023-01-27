
Birthday = input("Birthday?\nday/ month/ year")

Birthday.split(',')
a = Birthday[-1]
year = Birthday[6:10]

year=int(year)
print(year)
t =""
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    for x in range(2):
        for i in range(0,int(a)):
            t +="i"
        print("    __",t,"__")
        print("   |:H:a:p:p:y:|")
        print(" __|___________|__")
        print("|^^^^^^^^^^^^^^^^^^|")
        print("| :B:i:r:t:h:d:a:y:|")
        print("|                  |")
        print("~~~~~~~~~~~~~~~~~~~~")
else:
    for i in range(0,int(a)):
        t +="i"
    print("    __",t,"__")
    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^^|")
    print("| :B:i:r:t:h:d:a:y:|")
    print("|                  |")
    print("~~~~~~~~~~~~~~~~~~~~")