# ZADANIE 7.4.10
# Napisz program wyznaczający sumę n początkowych liczb pierwszych.

import math

def czy_pierwsza(liczba):
    for x in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % x == 0: return False
    return True

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if czy_pierwsza(x+1) is True:
        liczby.append(x+1)
        print(liczby)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")