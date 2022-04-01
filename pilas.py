class Nodo:
    def __init__(self,data):
        self.data = data
        self.siguiente = None
        

class Pila:
    def __init__(self):
        self.sup = None
        self.tamaño = 0
        
    def tamaño2(self):
        print(self.tamaño+1)
        
    def apilar(self,data):
        if self.sup == None:
            self.sup = Nodo(data)
            return
        nodo = Nodo(data)
        nodo.siguiente = self.sup
        self.sup = nodo
        self.tamaño +=1
        
    def expresiones(self):
        lista = []
        lista2 = []
        temp = self.sup
        while temp != None:
            if temp.data == '+':
                lista.append(temp.data)
            elif temp.data == '-':
                lista.append(temp.data)
            elif temp.data == '*':
                lista.append(temp.data)
            elif temp.data == '/':
                lista.append(temp.data)
            elif temp.data == '**':
                lista.append(temp.data)
            elif temp.data == ')':
                lista.append(temp.data)
            elif temp.data == '(':
                lista.append(temp.data)
            else:lista2.append(temp.data)
            temp = temp.siguiente
        print(lista)
        print(lista2)
        
    def imprimir(self):
        temp = self.sup
        while temp != None:
            print(f'{temp.data}',end=",")
            temp = temp.siguiente
        print("")
 
 
pila = Pila() 
pila.apilar(1)
pila.apilar(2)
pila.apilar('+')
pila.apilar(3)
pila.apilar('-')
pila.apilar(3)
pila.imprimir()

pila.expresiones()
####infija a postfija
