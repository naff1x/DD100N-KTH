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
    
        #inputList = 3*[None]
        inputList = []
        for i in range(3):
            #inputList[i] = input("("+ str(i) + ")" + " Write whatever in here: ")
            inputList.append(input("("+ str(i) + ")" + " Write whatever in here: "))
        print(inputList)
        del inputList[2]
        print(inputList)
        inputList.insert(2,3)
        print(inputList)
        for a in range(len(inputList)):
            print("Det finns " + str(a+1) + " värden i listan!")
        for input in inputList:
            print(input)
    
    def inputFunction(self):
        whatever = input(str("Skriv vad som helst här: "))
        print(whatever)
        siffra = float(input("Valfri siffra här: "))
        print(siffra)

Bc = BasicClass()
#Bc.testFunction()
#Bc.listFunction()
#Bc.inputFunction()