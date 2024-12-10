import time
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista_1000 = [random.uniform(1, 1000) for _ in range(1000)]
lista_10000 = [random.uniform(1, 1000) for _ in range(10000)]

inicio_1000 = time.time()
bubble_sort(lista_1000)
fim_1000 = time.time()

inicio_10000 = time.time()
bubble_sort(lista_10000)
fim_10000 = time.time()

print(f"{fim_1000 - inicio_1000:.5f} segundos para mil elementos")
print(f"{fim_10000 - inicio_10000:.5f} segundos para 10 mil elementos")
