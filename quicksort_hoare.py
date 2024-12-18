def quicksort(A, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        # Realiza a partição e obtém o índice do pivô
        p = hoare(A, lo, hi)
        # Ordena as duas partições
        quicksort(A, lo, p)     # O pivô é incluído na partição esquerda
        quicksort(A, p + 1, hi) # Partição direita

def hoare(A, lo, hi):
    # Escolhe o primeiro elemento como pivô
    pivot = A[lo]

    # Índices para partição
    i = lo - 1
    j = hi + 1

    while True:
        # Move o índice da esquerda para a direita enquanto A[i] < pivô
        while True:
            i += 1
            if A[i] >= pivot:
                break

        # Move o índice da direita para a esquerda enquanto A[j] > pivô
        while True:
            j -= 1
            if A[j] <= pivot:
                break

        # Se os índices se cruzarem, retorna o índice j
        if i >= j:
            return j

        # Troca os elementos nos índices i e j
        A[i], A[j] = A[j], A[i]

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Array original:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Array ordenado:", arr)
