range(10)

list(range(10))

(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

[]

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}



x = list(range(10))

# zadanie 1

[x + 6 for x in range(5)]

# Zadanie 2

t = [(x, str(x)) for x in range(15)]
print(t)

# zadanie 3

data = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
t = [x.upper() for x in data.keys() if data[x] > 5000]
print(t)

