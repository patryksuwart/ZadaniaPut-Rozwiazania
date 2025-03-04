# ZADANIE 7.4.8
# Napisz program wyznaczający sumę n początkowych liczb, których suma cyfr jest liczbą parzystą. Liczbę n
# należy pobrać od użytkownika.

def suma_cyfr(liczba):
    return sum(int(cyfra) for cyfra in str(liczba))

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if suma_cyfr(x+1) % 2 == 0:
        liczby.append(x+1)
        print(liczby)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")