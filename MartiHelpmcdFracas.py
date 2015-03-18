"""
hola, soc en Sistach. Investigo el mon del mcd en racionals
definim a, b i r	\in \Q
	q		\in \N
"""


# com a bon noob, comenzo per la definicio correcta
def cacamcd174 (a, b):
	while (b): a, b = b, a%b
	return a


"""
mcd (a, b) = mcs (a - qb, b)
llavors, com fem el modul?
El python no em fa el modul like
a = b * q + r
llavors ens toca implementar aquesta operacio
"""

class Rat:
	def __init__	(self, n, d = 1):
		self.numerador		= n
		self.denominador	= d

	def beautiful	(self):
		if self.numerador == 0: self.denominador = 1
		else:
			d = cacamcd174 (self.numerador, self.denominador)
			self.numerador		/= d
			self.denominador	/= d

# es un que no se fa anar... puamerra
	def prod	(self, e): # e \equiv entrada
		return cacamcd174 (self.numerador * e.denominador + self.denominador * e.denominador, self.denominador * self.numerador)
	
	def cacaRes	(self):
		return self.numerador / float (self.denominador)

	def resteta	(self, e):
		a = Rat ( (self.numerador * e.denominador) - (self.denominador * e.numerador), self.denominador * e.denominador )
		a.beautiful ()
		return a
	def QuansCopsUnAltre	(self, e):
		return int (self.cacaRes () / e.cacaRes () )
	
	def vegades (self, e):
		self.numerador *= e
	def __str__ (self):
		return str(self.numerador) + ' / ' + str(self.denominador)
	def isNull (self):
		return self.numerador


def modulMolonMarti (a, b): # retona la r, realment el que desitjem
# Marti Rubio Estrada, m'ha aconsellat de fer anar aquest algorithme
# a, b, r = q/w, e/t, y/u #mera posicio del teclat
# llavors tenim que r = ((a % b) * (w * t)) / (w * t)
# ho he testejat pel 5/7 % 2/4 i m'ha donat 3/14
# es el correcte ja que 3/14 + 1/2 = 5/7
# Com ue se m'ha ocorregut sense fer una multiplicacio i divisio estupida, on segeixo la definicio de modul,
# em quedare amb  el meu
	return 0

def modulMolona			(a, b):
	q = a.QuansCopsUnAltre	(b)
	#r = a.resteta		(b.vegades (q)), puta merda, no furule TT
	b.vegades		(q)
	r = a.resteta		(b)
	r.beautiful		()
	return r

def tstmodulMolona8321 ():
	a, b = Rat (5, 7), Rat (1, 2)
	print modulMolona (a, b)

def mcdRat (q, z, w, s):
	a, b = Rat (q, z), Rat (w, s)
	a.beautiful 				(		)
	b.beautiful 				(		)

	while (b.isNull ()): a, b = b, modulMolona (a, b)
	a.beautiful () # no te sentit fer un beautiful aqui... pero no fa el que vull aixi que mi  veig obligat
	return a

def tst (q = 5, w = 7, e = 2, r = 4): print mcdRat (q, w, e, r)

"""
Primer intent, un fracas total,
si poso els denominadors a 1, no fa el mcd com voldria. Alguna cosa ha fallat
Veurem futurs intents en un futur
"""
