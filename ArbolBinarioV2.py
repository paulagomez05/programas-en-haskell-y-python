# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:09:42 2018

@author: DAv_O
"""

class Nodo:
    def __init__(self,valor):
        self.info = valor
        self.izq  = None
        self.der  = None


class Abinario():
    def __init__(self):
        self.raiz = None

    def insertar (self, valor, raiz= None):    
        if (raiz == None):
            if (self.raiz == None):
                self.raiz = Nodo(valor)
                return 
            raiz = self.raiz
        
        print(raiz.info)        
        if (valor < raiz.info):
            if(raiz.izq == None):
                raiz.izq = Nodo(valor)
            else:
                self.insertar (valor, raiz.izq)
        else:
            if (raiz.der == None):
                raiz.der = Nodo(valor)
            else:
                self.insertar (valor, raiz.der)
                

    def preorden (self, raiz = None):
        if (raiz == None):
            if (self.raiz == None):
                return    
            raiz = self.raiz
        
        print (raiz.info)
        
        if (raiz.izq != None):
            self.preorden (raiz.izq)
        if (raiz.der != None):
            self.preorden (raiz.der)
             

    def inorden (self, raiz = None):
        if (raiz == None):
            if (self.raiz == None):
                return    
            raiz = self.raiz

        if (raiz.izq != None):
            self.inorden (raiz.izq)
            
        print (raiz.info)
        
        if (raiz.der != None):
            self.inorden (raiz.der)
            
            
    def postorden (self, raiz = None):
        if (raiz == None):
            if (self.raiz == None):
                return    
            raiz = self.raiz

        if (raiz.izq != None):
            self.postorden (raiz.izq)
            
        if (raiz.der != None):
            self.postorden (raiz.der)
            
        print (raiz.info)   

    def buscar(self, dato, raiz):
        if raiz == None:
            return None
        else:
            if dato == raiz.info:
                return raiz.info
            else:
                if dato < raiz.info:
                    return self.buscar(dato, raiz.izq)
                else:
                    return self.buscar(dato, raiz.der)

arbol = Abinario()
ejecucion = True

while ejecucion==True:
    
    print("ARBOL BINARIO")
    opc = input("\n1-Insertar nodo \n2-Preorden \n3-Inorden \n4-Postorden \n5-Buscar \n6-Salir \n\nEliga una opcion -> ")

    if opc == '1':
        print("Insertar")
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            arbol.insertar(nodo)
        else:
            print("\nSolo es Permitido ingresar digitos...")
               
    elif opc == '2':
        print("Recorrido Preorden")
        if arbol.raiz == None:
            print("Arbol Vacio")
        else:
            arbol.preorden(arbol.raiz)
            
    elif opc == '3':
        print("Recorrido Inorden")
        if arbol.raiz == None:
            print("Arbol Vacio")
        else:
            arbol.inorden(arbol.raiz)
            
    elif opc == '4':
        print("Recorrido Postorden")
        if arbol.raiz == None:
            print("Arbol Vacio")
        else:
            arbol.postorden(arbol.raiz)
            
    elif opc == '5':
        print("Buscar Nodo")
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if arbol.buscar(nodo, arbol.raiz) == None:
                print("\nNodo NO encontrado...")
            else:
                print("\nNodo encontrado -> ",arbol.buscar(nodo, arbol.raiz), " si existe...")
        else:
            print("\nSolo es Permitido ingresar digitos...")  
            
    elif opc == '6':
        print("\nElegiste salir...\n")
        ejecucion = False
        break
    else:
        print("\nOpcion NO VALIDA...")
    
    print()


