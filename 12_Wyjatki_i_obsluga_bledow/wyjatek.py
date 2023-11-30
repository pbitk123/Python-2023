l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")

l = 0
while True:
    try:
        l = input("podaj liczbe")
        l = int(l)
    except ValueError as e:
      #  print(e)
        print (f"{l} nie jest liczba")
else:
    break
    print('test')
suma = 0
i = l
while i > 0:
    suma += i%10
    i //= 10
    print(f'Suma cyfr podanej liczby {l} wynosi {suma}')


----------poprwne  rozwiazani
    liczba = 0
    while True:
        try:
            liczba = input("Podaj liczbę naturalną: ")
            liczba = int(liczba)
        except ValueError as e:
            print(f"{liczba} nie jest liczbą!")
        else: break
#    l = 14
    suma = 0
    i = liczba
    while i > 0:
        suma += i % 10
        i //= 10
    print(f'Suma cyfr podanej liczby {liczba} wynosi {suma}')

