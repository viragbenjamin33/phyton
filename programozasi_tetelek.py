# csere algoritmus
a = 5
b = 9
# cseréljük ki a és b változ értékét, egy segédváltozóval
c = a
a = b
b = c

print(a,b)

# pythonos megoldása a cserének

a, b = a, b
print(a,b)

# 1. sorozatszmítás tétele
x = [5,7,2,9,5,4]
summ = 0
for num in x:
  summ += num
print(summ)

# pythonos megoldás
print(sum(x))

# 2. eldöntés tétele
# döntsük el hogy van-e a listában 2-es szám

n = len(x)
i = 0
while i < n and x[i] != 2:
  i = i +1
if i < n:
  print("van benne 2-es")
else:
  print("nincs benne 2-es")
 
# pythonban ha meh akarjuk nézni hogy egy adott elem
# létezik-e a tömbben:

print(2 in x)

# 3. lineáris
# lényegében ugyanaz mint az eldöntés, csak ez az indexet
# adja vissza (hanyadik elem)

i = 0
while i < len(x) and x[i] != 2:
  i = i +1
if i < n:
  print("van benne 2-es és itt: {}".format(i))
else:
  print("nincs benne 2-es")

# pythonban ha indexe keresünk

print(x.index(2))

# 4. megszámlálás tétele
# számoljuk meg hogy hány darab páros szám van a listában

db = 0
for elem in x:
  if elem % 2 == 0:
    db += 1
print("{} darab páros szám van a listában".format(db))

# 5. maximum kiválasztás tétele
max_index = 0
for i, elem in enumerate(x):
  if x[i] > x[max_index]:
    max_index = i
print("A legnagyobb szám a listában: {}".format(x[max_index]))


# 6. buborék rendezés
# redezzük sorba az elemeket

n = len(x)
for i in range(n - 1):
  for j in range(0, n - i - 1):
    if x[j] > x[j+1]:
        # kicseréljük a j-edik és a j+1-edik elemet:
        x[j], x[j+1] = x[j+1], x[j]
# a megrendezett x tömb:
print(x)

x = [5,7,2,9,5,4]

# pythonban a lista rendezése
print(sorted(x))

x = [5,7,2,9,5,4]

# 7. minimum kiválasztásos rendezés

for i in range(0, n):
    min_index = i
    for j in range(i+1, n):
        if x[min_index] > x[j]:
            min_index = j
    x[i], x[min_index] = x[min_index], x[i]

print(x)

# 8. faktoriális rekurzív algoritmus

def fakt(n):
    if n == 0:
      return 1
    else:
      # rekurzív függvény: saját magát meghívja
      return n* fakt(n - 1)

print(fakt(4))