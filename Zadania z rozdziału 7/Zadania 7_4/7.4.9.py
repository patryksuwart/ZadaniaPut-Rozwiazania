# ZADANIE 7.4.9
# Napisz program wyznaczający sumę n początkowych liczb, których suma cyfr jest liczbą pierwszą. Liczbę n
# należy pobrać od użytkownika.

import math

def suma_cyfr(liczba):
    return sum(int(cyfra) for cyfra in str(liczba))

def czy_pierwsza(liczba):
    for x in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % x == 0: return False
    return True

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    t = suma_cyfr(x+1)
    if czy_pierwsza(t) is True:
        liczby.append(x+1)
        print(liczby)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")