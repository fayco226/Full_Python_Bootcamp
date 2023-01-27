#####################################
#      Exercice1                    #
#####################################

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictio = dict()
for a, b in zip(keys, values):
    dictio[a] = b

print(dictio)

#####################################
#      Exercice2                    #
#####################################

# Part 1

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price_TTC = 0
for j, i in family.items():

    if i <= 3:
        print(j, "must pay", 0)
        continue
    elif i <= 12:
        price_TTC += 10
        print(j, "must pay", 10, "$")
    else:
        price_TTC += 15
        print(j, "must pay", 15, "$")
print("\n The total Price which family must pay is ", price_TTC, "$\n")

# Part 2 Bonus
family = {}
n = int(input("Enter the number of people wants a ticket "))
for i in range(0, n):
    a = input("Enter a name of person")
    b = int(input("Enter age of personne"))
    family[a] = b
price_TTC = 0
for j, i in family.items():

    if i <= 3:
        print(j, "must pay", 0)
        continue
    elif i <= 12:
        price_TTC += 10
        print(j, "must pay", 10, "$")
    else:
        price_TTC += 15
        print(j, "must pay", 15, "$")
print("\n The total Price which family must pay is ", price_TTC, "$")

#####################################
#      Exercice3                    #
#####################################


brand = {"name": "Zara", "creation_date": 1975, "creator_name": "Amancio Ortega Gaona ",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 2, "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }}

print("Zaras clients are:")
for i in brand["type_of_clothes"]:
    print(i, end=' ')

brand["country_creation"] = "Spain"

k = "international_competitors"

if k in brand:
    brand[k].append("Desigual")

del brand["creation_date"]

print("the last international competitor are ", brand["international_competitors"][-1])
print("the major clothes colors in the US are ")
for i in brand["major_color"]["US"]:
    print(i, end=' ')

print("the amount of key value pairs are ", len(brand))
print("\n thekeys of dictionary are ")
for i in brand.keys():
    print(i, end=' ')

more_on_zara = {"creation_date": 1975, "number_stores": 10000}

brand.update(more_on_zara)

print(brand["number_stores"])  # number of store is update to 10 000

#####################################
#      Exercice4                    #
#####################################

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {users[i]: i for i in range(len(users))}
print(disney_users_A)

disney_users_B = {i: users[i] for i in range(len(users))}
print(disney_users_B)

disney_users = sorted(disney_users_A, reverse=False)
disney_users_C = {disney_users[i]: i for i in range(len(disney_users))}
print(disney_users_C)

disney_users_D = {users[i]: i for i in range(len(users)) if "i" in users[i]}
print(disney_users_D)

disney_users_E = {users[i]: i for i in range(len(users)) if users[i][:1] == "m" or users[i][:1] == "p"}
print(disney_users_E)
print("\n")