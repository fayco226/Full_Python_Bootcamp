
######################
#    Exercice 1      #
######################


print("Hellow world\n"*4)



######################
#    Exercice 2      #
######################

print(99**3*8)


######################
#    Exercice 3      #
######################

#   >>> 5 < 3   False
#
#   >>> 3 == 3 True
#
#   >>> 3 == "3" False
#
#   >>> "3" > 3  Traceback (most recent call last): File "<stdin>", line 1, in <module> TypeError: '>' not supported between instances of 'str' and 'int
#
# 
#  >>> "Hello" == "hello"  False


######################
#    Exercice 4      #
######################

computeur_hand = "DELL"

print("I have a",computeur_hand,"computer")

######################
#    Exercice 5      #
######################

name = "Lengane Abdoul Faîcal"
age = 22
shoe_size = 30
info = "I'am {} i've {} years and {} is  my shoe size ".format(name,age,shoe_size)
print(info)

######################
#    Exercice 6      #
######################

a = 4
b = 3
if a>b:
    print("helow world")


######################
#    Exercice 7      #
######################

a = int(input("enter a number"))

if a%2 == 0:
    print("number is odd")
else:
    print("number is even")


######################
#    Exercice 8      #
######################

her_name = input("What's your name")
my_name = "Lengane Abdoul Faîcal"
if her_name == my_name:
    print("you and me have same name") 
else:
    print("you and me haven't same name")


######################
#    Exercice 9      #
######################

her_height = float(input("what's your height in inches: "))
her_height *= 2.54
if her_height < 145:
    print("You are tall to enough ride")
else:
    print("You need to grow some more to ride")
