import time

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
arr = list(range(1000, 1, -1))
print("Lista:")
print(arr[:10])
inicio = time.time()
bubble_sort(arr)
fim = time.time()
print("Lista depois de organizar:")
print(arr[:10])
print(f"A duração de execução foi de: {fim - inicio:.6f} segundos")

