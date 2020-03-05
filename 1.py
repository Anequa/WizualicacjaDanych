print("hello world")

tekst="hello world"
tekst='hello world'
tekst="""hello world"""
print(tekst)
#tekst=0
print(tekst)
print(type(tekst))
print(type(5))
print(type(5.5))
print(type(True))
print(type(None))

print(5//5)#dzielenie bez reszty
print(5%5)#modulo
print(5**5)#potegegowanie
print("ala"+" ma kota"+str(5)+"lat")#konkatenacja
liczba=int("100")
print ("ala"*10)
lista =[]
print(type(lista))
lista2=[1,2,3]
print(lista2[0])
imie='Magdalena'
print(imie[0])
lista2[0]=5
print(imie.swapcase())#tylko wyswietleniie
imie=imie.swapcase()#nadpisanie
print(imie)
"Ala".swapcase()
lista3=[1,"ala",4.5,None,True,[1,2]]
print(lista3[5][1])
macierz=[
    [2,4,5],
    [3,1,5],
    [6,7,8]
]
macierz[1][1]#1
nowa=lista2+macierz
#słownik
slownik={}
slownik['imie']='adam'
slownik[0]='adam'
print(slownik)

slownik2={'imie' :'adam',0: "adam"}
print(slownik2.keys())
print(slownik2.values())

# def pow():
#     pass
# for element in kolekcja

# from math import*
# import math as m
# from math import pow 
# m.pow(2,2)
# m.pi




