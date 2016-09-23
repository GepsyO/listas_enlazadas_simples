# listas_enlazadas_simples
#Ver en dirección: https://repl.it/X3G/4277
#Autor Gepsy Ortiz.

# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
		
		
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0


    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info 
			nodo=nodo.sig		
	
  #Metodo pos
	def pos_actual (self,pos):
		nodo=self.__primero
		cont=0
		while(nodo!= None):
			if (cont==pos):
				return
			nodo=nodo.sig
			cont=cont+1
		if (nodo==self._ultimo):
			return
		

	def buscar_elem(self,valor):
		p=0
		nodo=self.__primero
		while(nodo!= None):
			if(nodo.info==valor):
				return p
			nodo=nodo.sig
			p=p+1
		return -1

	def eliminar_primero(self):
		if(self.__primero==None):
			return
		nodo=self.__primero
		self.__primero=nodo.sig
		self.__n=self.__n-1
		self.__pos=self.__pos-1
		del nodo

		if(self.__n==0):
			self.__ultimo=None
			self.__actual=None


	#Metodo que verifica si son elementos repetidos
	def elem_repetidos(self):
		if(self.__primero==None):
			return
		
		nodo=self.__primero
		for i in range (self.__n-1):
			temp=nodo.sig
			for j in range (self.__n-1):
				if(nodo and temp != None):
					if(nodo.info == temp.info):
						return "repetidos"
					else:
						temp=temp.sig
			nodo=nodo.sig
		return "nooooo"



	#Metodo que verifica si los elementos son ordenados
	def elem_ordenados(self):
		if(self.__primero==None):
			return
		
		nodo=self.__primero
		for i in range(self.__n-1):
			temp=nodo.sig
			for j in range (self.__n-1):
				if(nodo.info < temp.info):
					temp=temp.sig
					
				else:
					return "no son ordenados"
					
		nodo=nodo.sig
		return "si son ordenados"
	
		
	#metodo para sumar elem enteros
	def elem_enteros(self):
		if(self.__primero== None):
			return
		suma=0
		nodo=self.__primero
		for i in range(self.__n):
			if(type(nodo.info) == int):
				suma=suma + nodo.info
				nodo= nodo.sig
			else:
				nodo= nodo.sig
		return suma



	#metodo para comparar 2 listas
	def comp_lista(self,lista):
		lista=lista.__primero
		nodo=self.__primero
		cont=0
		for i in range (self.__n-1):
			if(lista.info != nodo.info):
				cont=cont+1

			else:
				cont=cont-1	
				
		nodo=nodo.sig
		lista=lista.sig
		if(cont<1):
			return True
		else:
			return False					
			
			
# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(1);
l.insertar_actual(2);
l.insertar_actual(4);
l.insertar_actual(10);


new= Lista()
new.insertar_actual(1);
new.insertar_actual(2);
new.insertar_actual(4);
new.insertar_actual(10);
""""print l.comp_lista(new)
"""
"""print l.elem_enteros()
print new.elem_enteros()
"""
print l.elem_repetidos()
print l.elem_ordenados()
