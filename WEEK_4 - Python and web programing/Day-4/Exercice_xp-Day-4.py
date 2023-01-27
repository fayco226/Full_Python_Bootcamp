# Exercice 1

def display_message():
  print("We are learning the fullstack python django bootcamp")

display_message()

# Exercice 2

def favorite_book(title):
  print(f"One of my favorite books is {title}")
favorite_book("40 RULES OF LOVE (D’ELIF ŞAFAK)")

# Exercice 3

def describe_city(city, country):
  print(f"{city} is in {country}")
describe_city("Ouagadougou", "BURKINA FASO")

# Exercice 4


import random
from random import randint
def randomNumber(z):
    Numb = random.randint(1, 100)
    if z == Numb:
        print(f" Success!!! \n number {z} and the random number {Numb}")
    else:
        print(f" failure... The user number is {z} and the random number is {Numb}")
    randomNumber(99)

# Exercice 5

def make_shirt(size=150, text="I like Python"):
  print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()

# Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for i in range(len(magician_names)):
        print(magician_names[i])

def make_great():
    for i in magician_names:
        i = i + " the Great"
        print(i)
make_great()

#Exercice 7
import random
from random import randint


def get_random_temp(season):
    if season == "winter":
        value = random.randint(0, 16)
    elif season == "fall":
        value = random.randint(16, 23)

    elif season == "spring":
        value = random.randint(24, 32)

    elif season == "summer":
        value = random.randint(32, 40)
    else:
        value = random.randint(-10, 0)
    return value


def main():

    season = input("Please enter your current season: ")
    if season == season:

        randtmp = get_random_temp(season)
        print(f"the current temperature is {randtmp} degree celsus and us in{season}")
        if randtmp < 0:
            print("Brrr, it's freezing! Wear extra layers today")
        elif randtmp >0 and randtmp < 16:
            print("Quite cold ! Don't forget your coat")
        elif randtmp >=16 and randtmp <= 23:
            print("A bit cool even if the weather is nice")
        elif randtmp >=24 and randtmp < 32:
            print("Very good weather")
        elif randtmp >=32 and randtmp < 40:
            print("It's hot")
        else:
            print("Bad weather too hot")
    else:
        print("no season")
main()