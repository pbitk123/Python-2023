n = 5

while n > 0:
    print(n)
    n -= 1

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')



n = 100
while n > 0:
    n -= 1
    suma_liczb = ( n % 10 + n // 10)
     if (suma_liczb %7 == 0 ) and (n % 2 == 0):
        print(n)
     else:
        print('Zla liczba')


i=0
while i<100:
    i+=1
    if i % 2 == 0 and (i % 10 + i // 10) % 7 == 0:
        print(i)
        continue
else:
    print('Koniec')


suma=0
i = input("podaj liczbe")
for c in i:
    suma += int(c)
print(f'{suma}')


liczba = input("Podaj liczbe")

suma_liczb = 0
for g in liczba:

    suma_liczb += int(g)

print(f"suma liczby{liczba} wynosi:{suma_liczb}")



n = int(input("Podaj liczbę:"))
print(f'Podałeś liczbę {n}')

suma = 0
while n > 0:
    suma += n % 10
    n //= 10

print(suma)




