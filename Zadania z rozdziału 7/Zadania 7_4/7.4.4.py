# ZADANIE 7.4.4
# Napisz program wyznaczający sumę n początkowych liczb podzielnych przez 7. Liczbę n należy pobrać od
# użytkownika.

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if (x+1) % 7 == 0: liczby.append(x+1)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")
print(liczby)