# ZADANIE 7.4.5
# Napisz program wyznaczający sumę n początkowych liczb kończących się cyfrą 1, 2 lub 7. Liczbę n należy
# pobrać od użytkownika.

liczba_max = int(input("Podaj liczbę: "))
liczby = []

for x in range(liczba_max):
    if str((x+1)).endswith("1") or str((x+1)).endswith("2") or str((x+1)).endswith("7"):
        liczby.append(x+1)

print(f"Suma {liczba_max} początkowych: {sum(liczby)}")
print(liczby)