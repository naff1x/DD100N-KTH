# -*- coding: utf-8 -*-
print("Program booted, beep boop!")

from random import randint

class BasicClass():

    def testFunction(self):
        print("You made it!")
    def listFunction(self):
        lista = [0,1,2,3,4]
        #print(lista)
        sorteradLista = sorted(lista, reverse = True)
        #print(sorteradLista)
        #print(lista)

        matris = []
        matris.append(lista)
        matris.append(sorteradLista)
        print(matris[0][4])
    
        inputList = 3*[None]
        for i in range(3):
            inputList[i] = input(str("Enter input: "))

        print(inputList)
        del inputList[2]
        print(inputList)
        inputList.insert(2,3)
        print(inputList)
        for a in range(len(inputList)):
            print("Det finns " + str(a+1) + " värden i listan!")
        for value in inputList:
            print(value)
    
        cityList = []
        cityList.append("Stockholm")
        cityList.append("London")
        cityList.append("New York")

        for city in cityList:
            print(city)

    def inputFunction(self):
        whatever = input(str("Skriv vad som helst här: "))
        print(whatever)
        siffra = float(input("Valfri siffra här: "))
        print(siffra)
    def dictionaryFuntion(self):
        ageDict = {"Linus":16, "Alex":17, "Albert":"too damn old"}
        query = input(str("I sure hope you're not a pedofile or anything, who are you thinking about?: "))
        print(str(query) + " is " + str(ageDict[query]))
        nameToDel = input(str("Who do you want to delete from the database?: "))
        del ageDict[nameToDel]
        print(ageDict)
        input("Almost done")
        print(ageDict.keys())

        for key in ageDict.keys():
            print(str(key) + " ger värdet: " + str(ageDict[key]))
    def bigDictFunction(self):
        databas = {}
        nycklar = []
        värden = []
        siffror = [1,2,3]
        översattEtt = ["ett","one","uno"]
        översattTvå = ["två","two","dos"]
        översattTre = ["tre","three","tres"]

        for i in range(len(siffror)):
            nycklar.append(siffror[i])
        
        värden.append(översattEtt)
        värden.append(översattTvå)
        värden.append(översattTre)

        for i in range(3):
            databas[nycklar[i]] = värden[i]

        print(databas)
    def parameterFunction(self, message = "Null?", number = 16):
        print(message, number)
    def randomFunction(self):
        import random

        slumpTal = random.randint(1,9)
        print("Du kastar en tärning...", end=" ")
        print("och får " + str(slumpTal) + "!")
    def mathFunction(self):
        import math

        bas = int(input("Ange bastal: "))
        exponent = int(input("Ange exponent: "))
        print("Svaret blir: " + str(math.pow(bas,exponent)))
    def moduleTestFunction(self):
        testInt = randint(0,9) # funktionen 'randint' kan kallas utan 'random'
        print(testInt)         # eller lokal import tack vare en tidigare import
    def fileReader(self, flag=0):
        fileMessage = []
        if flag is 0:
            textFile = open("text.txt", "r")
            #textFile = open("text.txt", "r", encoding="utf-8")
            for line in textFile:
                fileMessage.append(line)
            textFile.close()
            print("flag was 0")
        else:
            with open("readText.txt", "r", encoding="utf-8") as file:
                for rad in file:
                    fileMessage.append(rad)
            print("flag was 1")
        print(fileMessage)
    def fileWriter(self):
        with open("writtenFile.txt", "w", encoding="utf-8") as skrivFil:
            skrivFil.write("Rad ett\nRad två\nRad tre")
Bc = BasicClass()
#Bc.testFunction()
#Bc.listFunction()
#Bc.inputFunction()
#Bc.dictionaryFuntion()
#Bc.bigDictFunction()
#Bc.parameterFunction()
#Bc.randomFunction()
#Bc.mathFunction()
#Bc.moduleTestFunction()
#Bc.fileReader(0)
Bc.fileWriter()