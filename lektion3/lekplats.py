# -*- coding: utf-8 -*-

lista = [0,1,2,3,4]
#print(lista)
sorteradLista = sorted(lista, reverse = True)
#print(sorteradLista)
#print(lista)

matris = []
matris.append(lista)
matris.append(sorteradLista)
print(matris[0][4])

class BasicClass():
    def testFunction(self):
        print("You made it!")

bC = BasicClass()
bC.testFunction()
