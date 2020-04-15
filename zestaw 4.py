import sys

##1
# podzielne=[x*4 for x in range(1,100,1)]
# print (podzielne)
# plik=open("l.podzielne.txt","w+")
# plik.writelines(str(podzielne))
# plik.close()  
##zad2
# plik=open("l.podzielne.txt","r")
# odczyt=plik.read()
# plik.close()
# print(odczyt)
##zad3
# slowo=("jakies slowa")
# with open("l.podzielne.txt","a+") as plik:
#     tekst=sys.stdin.readline()
#     plik.write(str(tekst))

#     plik.write(str(slowo))
#     plik.seek(0,0)
#     for linia in plik:
#         print (linia)
##zad4
# class Zakupy:
#     def __init__(self,n_p,il,jed,cena):
#         self.nazwa_produktu=n_p
#         self.ilosc=il
#         self.jednostka=jed
#         self.cena=cena
#     def wyswietl_produkt (self):
#         print("nazwa",self.nazwa_produktu)
#         print("ilosc",self.ilosc)
#         print("jednostka",self.jednostka)
#         print("cena",self.cena)
#     def ile_produktu(self):
#         print ("ile produktu:",self.ilosc,self.jednostka)
#     def ile_kosztuje(self):
#         print("koszt:",self.cena*self.ilosc, "zł") 
# sklep=Zakupy("jajka",2,"sztuki",0.20)
# Zakupy.ile_produktu(sklep)    
# Zakupy.ile_kosztuje(sklep)  
##zad5
class ciagi :
    a1=0
    r=0
    n=0

    def wyswietl_dane(self):
        print(self.a1,self.r,self.n)

    def pobierz_elementy(self,*wartosci_ciagu):
        self.a1=wartosci_ciagu[0]
        self.wartosci_ciagu=wartosci_ciagu

    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n

    def policz_sume(self):
        return self.n*((2*self.a1)+((self.n-1)*self.r)/2)

    def policz_elementy(self):
        for i in range (self.n):
            print("a",i+1,"=",self.a1+(self.r*i))


