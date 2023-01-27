##############################
#        Exercice1           #
##############################

my_fav_numbers = {1, 9, 58, 85}
my_fav_numbers = set(list(my_fav_numbers))

my_fav_numbers.add(4)
my_fav_numbers.add(5)
print(my_fav_numbers)
my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)
friend_fav_numbers = set()
friend_fav_numbers.add(12)
friend_fav_numbers.add(55)

our_fav_numbers = set(list(my_fav_numbers) + list(friend_fav_numbers))

print(our_fav_numbers)


#############################
#        Exercice2          #
#############################
tu = (1, 4, 6, 8, 9)  # tuple which value is integers

# No! it isn't possible to add more integers to the tuple

#############################
#        Exercice3          #
#############################

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)  # we have two Apples in the list
basket.clear()
print(basket)

#############################
#        Exercice4          #
#############################
# 3
t = list()
i = 1
while i <= 4:
    i = i+0.5
    t.append(i)
print(t)

#############################
#        Exercice5          #
#############################
#1
for i in range(1, 21):
    print(i)
#2
for i in range(1,21):
    if i%2 == 0:
        print(i)

#############################
#        Exercice6          #
#############################
while True:
    their_name = input("Write Your name ")
    if their_name == "Faycal":
        break
     
#############################
#        Exercice7          #
#############################
#1
favorite_fruits = input("Enter your favorites fruits separate by single space    ")
#2

favorite_fruits = favorite_fruits.split(" ")

any_frruit = input("Enter a name of any fruit")

if any_frruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

#############################
#        Exercice8          #
#############################
topping_pizza = list()
while True:
    t = input("enter a series of pizza toppings, if you finish input quit  ")
    if t == 'quit':
        break
    else:
        print("we shall add that topping to their pizza.")
        topping_pizza.append(t)
print("All the toppings on the pizza : ")
price = 10
for s in topping_pizza:
    print("-",s)
    price += 2.5
print("And price is  ", price)

#############################
#        Exercice9          #
#############################

n = int(input("How many people wants a ticket \n"))
print("Enter the age of each person who wants a ticket.\n")
price_TTC = 0
for i in range(0,n):
    print("Enter the age of",i ,"person who want a ticket.")
    each_age = int(input(" "))
    if each_age <= 3:
        continue
    elif each_age <=12:
        price_TTC += 10
    else:
        price_TTC +=15
print("\n The total Price is ", price_TTC)
teenagers_list = input("Enter the teenagers names list separate by simple space ")
teenagers_list = teenagers_list.split(" ")

for i in teenagers_list:
    print("What is the age of ", i)
    teenager_age = int(input(" "))
    if teenager_age<16 or teenager_age>21:
        teenagers_list.remove(i)
print("The final list of teenagers is")
for i in teenagers_list:
    print(i)
    
    
#############################
#        Exercice10         #
#############################

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for i in range(0, len(sandwich_orders)):
    finished_sandwiches = sandwich_orders.pop(i)

print(sandwich_orders)
print(finished_sandwiches)