import math

def fact(n):
    k = 1
    while k <= n:
        yield math.factorial(k)
        k += 1

while True:
    try:
        n = int(input('Введите число:'))
        break
    except ValueError:
        print('Совет дня: попробуйте все же ввести число')

for el in fact(n):
    print(el)
