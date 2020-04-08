#zad1
# A=[1/x for x in range (1,11)]
# print (A)

# B=[2**x for x in range (11)]
# print (B)

# C=[x for x in B if x%4==0]
# print (C)
#zad2

   
# from random import random
# M=[[round(random()*1000) for y in range(1+4*x,5+4*x)] for x in range(4)]
# print(M)
# przekatna=[M[x][x]for x in range(4)]
# print(przekatna)


# #zad 3
# amku={"Czekolada":"sztuki", "lody":"sztuki","reesee's":"paczki"}
# print(amku)
# amkuNaOdwrót={key for key in amku if amku[key]=="sztuki"}
# print(amkuNaOdwrót)

#zad 4
# import math

# def funkcja(a,b):
#     if (a>0):
#         print("rosnie")
#     elif (a<0):
#         print("maleje")
#     else:
#         print("stala")

# c=int(input('podaj a:'))
# d=int(input('podaj b:'))
# print(funkcja(c,d))

#zad5
# def równoległe (a,b,c,d):
#     if (a==c):
#         print ("równoległe")
#     elif (a*c==-1):
#         print("prostopadłe") 
#     else :
#         print("anitaka anitaka")
# a=int(input("podaj a f1"))    
# b=int(input("podaj b f1"))  
# c=int(input("podaj a f2"))  
# d=int(input("podaj b f2"))   
# print(równoległe(a,b,c,d))
#zad 6
# import math
# def kolo (a=1,b=1,x=2,y=2):
#     r=math.sqrt((x-a)**2+(y-b)**2)
#     print(r)

# print(kolo())
#zad 7
# import math

# def fun(a=4,b=3):
#     c=math.sqrt(a**2+b**2)
#     print (c)
# print(fun())

##zad 8
# def aryt(a=1,r=1,ile=10):
#     s=((2*a+(ile-1)*r)/2)*ile
#     print(s)
# print(aryt())
##or
# def aryt (a=1,r=1,ile=10):
#     suma=0
#     x=a
#     for i in range(ile):
#         suma=suma+x
#         x=x+r
       
       
#     return suma
# print(aryt())

##zad9
# def ciag(*licz):
#     if(len(licz)==0):
#         return 0
#     else:
#         iloczyn=1
#         x=1
#         for i in licz:
#             iloczyn=iloczyn*i
#         return iloczyn
# print(ciag(1,2,4))
##zad10
# def sklep(**produkty):
#     suma=0
#     for x in produkty:
#         suma=suma+produkty[x]
#     return suma 
# print(sklep(marchew=4,cos=2,inne=6))








