# ZADANIE 7.1.5
# Napisz program drukujący na ekranie literę L złożoną z literek L. Wielkość litery A (jej szerokość,
# wysokość i grubość) wczytujemy z klawiatury. Przykładowa litera ma wymiary: grubość=4, wys=11, szer=8.
#
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLL
# LLLLLLLL
# LLLLLLLL
# LLLLLLLL
# LLLLLLLL

szerokosc = int(input("Podaj szerokość litery L: "))
wysokosc = int(input("Podaj wysokość litery L: "))
grubosc = int(input("Podaj grubość litery L: "))

for l in range(wysokosc):
    if l < wysokosc - grubosc:
        print('L' * grubosc)
    else:
        print('L' * szerokosc)