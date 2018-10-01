# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:04:13 2018

@author: DAv_O
"""
import numpy as np

lista = [5,4,7,8] 
lista2 = [1,2,3,4,5,6]   

def sumar(lista):
      if len(lista) == 1:
          return lista[0]
      elif len(lista)==0:
          return 0      
      else:
          return lista[0] + sumar(lista[1:])

def invertir(lista):
    if lista:      
        return lista[::-1] 
    else:
        return 0
                       
def comparar(listaA,listaB):
    return np.all(np.array(listaA) == np.array(listaB))

def comprobarOrden(lista):
    return all(b >= a for a, b in zip(lista, lista[1:]))

def buscarUbicacion(lista,posicion):
    if posicion< len(lista):
        return lista[posicion]
    else:
        return "Posicion Invalida"

def mayorElemento(lista):
    if lista:    
        return lista[np.argmax(lista)]
    else:
        return 0    
    
def contarPares(lista):  
    pares=0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            pares +=1
    
    return pares
    
def cuadrados(lista):
    cuadrados=[]
    for i in range(len(lista)):
        cuadrados.append(lista[i]*lista[i])
    
    return cuadrados

def divisibles(lista,divisor):  
    divisibles=[]
    for i in range(len(lista)):
        if lista[i]%divisor == 0:
            divisibles.append(lista[i])
    
    return divisibles

def esPrimo(num):
    if num < 2:     
        return False
    for i in range(2, num):  
        if num % i == 0:    
            return False
    return True



def primos(limite):
    
    primos=[]
    for i in range(limite):
        if esPrimo(i)== True:
            primos.append(i)
    
    return primos
    
    
    
   
print(sumar(lista))
print(invertir(lista))
print(comparar(lista,lista))
print(comprobarOrden(lista2))
print(buscarUbicacion(lista,2))
print(mayorElemento(lista))
print(contarPares(lista2))
print(cuadrados(lista2))
print(divisibles(lista,1))
print(primos(100))
