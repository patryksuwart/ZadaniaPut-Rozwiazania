# ZADANIE 7.1.11
# Napisz program drukujący na ekranie trójkąt. Wysokość trójkąta wczytujemy z klawiatury. Poniższy trójkąt
# ma wysokość wys=5.
#       X
#      XX
#     XXX
#    XXXX
#   XXXXX

wysokosc = int(input("Podaj wysokość trójkąta: "))

for x in range(wysokosc+1):
    print(' ' * (wysokosc-x) + 'X' * x)