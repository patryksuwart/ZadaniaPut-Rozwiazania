# ZADANIE 7.4.6
# Napisz program wyznaczający sumę n początkowych liczb kończących się liczbą 31, 62 lub 17. Liczbę n
# należy pobrać od użytkownika.

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if str((x+1)).endswith("31") or str((x+1)).endswith("62") or str((x+1)).endswith("17"):
        liczby.append(x+1)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")
print(liczby)