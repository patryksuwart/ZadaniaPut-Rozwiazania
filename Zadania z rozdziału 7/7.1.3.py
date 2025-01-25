# ZADANIE 7.1.3
# Napisz program drukujący na ekranie prostokąt z literek X. Wysokość i szerokość prostokąta wczytujemy z
# klawiatury:
# XXXXXXXXXX
# X        X
# X        X
# XXXXXXXXXX

wysokosc = int(input('Podaj wysokość: '))
szerokosc = int(input('Podaj szerokość: '))

for x in range(wysokosc):
    if x == 0 or x == wysokosc-1:
        print('X' * szerokosc)
    else:
        print(f"X{' '*(szerokosc-2)}X")