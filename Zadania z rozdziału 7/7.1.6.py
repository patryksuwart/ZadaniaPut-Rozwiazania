# ZADANIE 7.1.6
# Napisz program drukujący na ekranie prostokąt z literek X. Wysokość i szerokość prostokąta wczytujemy z
# klawiatury. Poniższy prostokąt ma wymiary: szer=10, wys=4.
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX

wysokosc = int(input('Podaj wysokość prostokąta: '))
szerokosc = int(input('Podaj szerokość prostokąta: '))

for x in range(wysokosc):
    print('X' * szerokosc)