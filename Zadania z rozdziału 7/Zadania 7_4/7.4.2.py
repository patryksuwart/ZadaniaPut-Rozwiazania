# ZADANIE 7.4.2
# Napisz program wyznaczający sumę n początkowych liczb nieparzystych. Liczbę n należy pobrać od
# użytkownika.

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if (x+1) % 2 != 0: liczby.append(x+1)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")
print(liczby)