import random
import sys
__author__ = 'Marva'

dict = {"Mis on karu?":"0",
        "Kui pikk?":"1",
        "Midagi huvitavat veel?":"aha"
        }

orderOfQuestion = input("True for same and False for random")
i=0

while True:
    if orderOfQuestion==True:
        kysimus = random.choice(list(dict.keys()))
    else:
        kysimus = print(dict[i])

    vastus = input(kysimus)
    if vastus=="":
        print("Vastus: "+dict[kysimus])
        continue
    i+=1



print (dict["Kui pikk?"])