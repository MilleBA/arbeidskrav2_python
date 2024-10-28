# Arbeidskrav 2 IKKE FERDIG (oppg 5, 1?, 3?)

# Oppgave 1

import datetime

alder = int(input("Hvilket år er du født?"))

dato = datetime.datetime.now()

def count_age():
    age = int(dato.year - alder)
    print("Du er ", age, " år gammel.")
    
count_age()

# display?


# Oppgave 2

import math

antall_elever = int(input("Skriv inn antall elever:" ))

def count_pizza():
    person_pizza = 0.25
    pizza = math.ceil(antall_elever * person_pizza)
    print("Det må handles inn ", pizza, " pizzaer til festen.")
    
count_pizza()

# Oppgave 3
# Grader til radianer

import numpy as np
v_grad = float(input("Skriv inn gradtallet:" ))
v_rad = v_grad*np.pi/180 # Radiantallet til vinkelen

print("Radiantallet til vinkelen: ", v_rad)

# Import math Library and convert different degrees into radians
import math
print("Radiantallet til vinkelen: ", math.radians(v_grad))


# Oppgave 4
# Keys - land, hovedstaden, antall innbygere i mill. i hovedstaden

# a)
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# b)

def capitalize(name):
    formatert_name = name[0:1].capitalize() + name[1:]
    return formatert_name

def get_country():
    landInput = input("Skriv et land:")
    land = capitalize(landInput)
    return land

def write_country():
    land = get_country()
    
    if land in data:
        hovedstaden = data[land][0]
        innbygere = data[land][1]
        print(hovedstaden, " er hovedstaden i ", land, " og det er ", innbygere, " mill. innbygere i ", hovedstaden)
    else:
        print("Landet er ikke i databasen.")
        
write_country()

# c) 

def update_country():
    land = get_country()
    
    while land in data:
        land = get_country()
    
    if land not in data:
        hovedstaden = input("Skriv hovedstaden:")
        innbygere = input("Skriv antall innbygere i mill. i hovedstaden:")
        data[land] = [capitalize(hovedstaden), float(innbygere)]
        print(data)
    else:
        print("Det oppstod noen feil underveis.")

update_country()

# Oppgave 5


# Oppgave 6

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -x**2 - 5

x_verdier = np.linspace(-10, 10, 200) # 200 punkter jevnt fordelt på intervallet [-10,10]
y_verdier = f(x_verdier)

plt.plot(x_verdier, y_verdier, label ="f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graf av funksjonen f(x) = -x^2 - 5")
plt.legend()
plt.grid(True)
plt.show()

    