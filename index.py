
# 6
def dodatnie(listadodatnia):
    listawynik = []
    for i in listadodatnia:
        if i > 0:
            listawynik.append(i)
    return listawynik

listadodatnia = (0, 5, 10, -5, 3)
# print(dodatnie(listadodatnia))

# 7
def przecena(cena, rabat):
     if cena >= 0 and rabat > 0 and rabat < 101:
          return round(cena * (1 - rabat / 100), 2)
     else:
          return None

# print(przecena(99, 2))

# 8

slownik = {
     "Wszystkie znaki": " ",
     "Liczba słów": " ",
     "Liczba spacji": " "
}

def	statystyki(zdanie ,slownik):
	znaki = len(zdanie)
	slowa = len(zdanie.split())
	spacje = zdanie.count(" ", 0, len(zdanie))

	slownik["Wszystkie znaki"] = znaki
	slownik["Liczba słów"] = slowa
	slownik["Liczba spacji"] = spacje
	return slownik

# print(statystyki("Randomowe zdanie xd", slownik))

# 9
def srednia(*liczby):
	cyfry = int()
	i = 0
	for liczby in liczby:
		cyfry += liczby
		i += 1
	wynik = cyfry / i
	return wynik

# print(srednia(10, 21, 654, 234, 234))


# 10
def walec(promien, wysokosc):
	def kolo(promien):
		return 3.14 * (promien ** 2) 
	polekola = kolo(promien)
	polewalca = 2 * polekola + (2 * 3.14 * promien * wysokosc)
	return float(polewalca)

print(walec(4, 6))
