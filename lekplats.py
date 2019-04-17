# -*- coding: utf-8 -*-

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

Bc = BasicClass()
#Bc.testFunction()
Bc.listFunction()
#Bc.inputFunction()
#Bc.dictionaryFuntion()