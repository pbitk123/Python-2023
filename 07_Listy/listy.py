l = [3, 5, 6, 7]
l

l[1]
l[0]
len(l)
l[0:2]
l[1:2]
l[1:]
l[:2]
l[-1]
l[1:-1]
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop()
l

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'

'.' in s2
3 in l

'.' in s2



l.insert(100,2)

l.insert(2,100)



i = input('podaj text')
l = []

 for n in i:
     l.append(i)
     print(l)


napisy = []

while True:
    napis = input("Wprowadź dowolne słowo: ")

    if not napis:
        break

    napisy.append(napis)

napisy.sort()
print(napisy)


liczby = []

while True:
    liczba = int(input("Wprowadź dowolne liczbe: "))

    if liczba % 2 != 0:
        break

    liczby.append(liczba)
liczby.sort()
liczby.pop()
print(liczby)

###zadanie

lista = []
parzysta = 0
while True:
    element = input("Wprowadź dowolne liczbe: ")
    if not element:
        break
    lista.append(element)
lista.sort(reverse=True)
for a in lista:
    if (int(a) % 2 == 0):
        parzysta =a
        break

print(parzysta)

l = []
while True:
    liczba = input("Podaj liczbę, a dodam ją do listy: ").strip()
    if liczba == "":
        break
    l.append(int(liczba))
l.sort()
for i in range(1, len(l)):
    if l[-1*i]%2 == 0:
        print(f"Ostatnia parzysta liczba to: {l[-1*i]}")
        break

