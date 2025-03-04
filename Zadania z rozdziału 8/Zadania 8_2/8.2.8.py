# ZADANIE 8.2.8
# Ile razy w podanym ciągu liczb wystąpił drugi co do wielkości najmniejszy element ciągu?

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []
ile = 0

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

najmniejsza = min(liczby)

for x in range(len(liczby)):
    if najmniejsza in liczby: liczby.remove(min(liczby))
    else: break

for l in liczby:
    if l == min(liczby):
        ile += 1

print(f'Liczba większa od najmniejszej: {min(liczby)}')
print(f'Wystąpiła: {ile}', end = ' razy' if ile > 1 else ' raz')