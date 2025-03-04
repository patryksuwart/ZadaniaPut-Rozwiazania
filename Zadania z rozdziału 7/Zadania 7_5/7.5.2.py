# ZADANIE 7.5.2
# Napisz program wyznaczający wartość n! Zadanej liczby n. Liczbę n należy pobrać od użytkownika.

silnia = int(input("Podaj liczę n!: "))
wynik = 1
liczby = []

for x in range(silnia):
    liczby.append(x+1)

for l in liczby:
    wynik = l * wynik

print(f"Silnia {silnia} początkowych: {wynik}")
print(liczby)