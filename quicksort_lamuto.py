def quicksort(A, lo, hi):
    # Verifica se os índices são válidos
    if lo >= hi or lo < 0:
        return

    # Realiza a partição e obtém o índice do pivô
    p = lamuto(A, lo, hi)
    
    # Ordena as duas partições
    quicksort(A, lo, p - 1)  # Lado esquerdo do pivô
    quicksort(A, p + 1, hi)  # Lado direito do pivô

def lamuto(A, lo, hi):
    # Escolhe o último elemento como pivô
    pivot = A[hi]

    # Índice temporário do pivô
    i = lo

    for j in range(lo, hi):
        # Se o elemento atual é menor ou igual ao pivô
        if A[j] <= pivot:
            # Troca o elemento atual com o elemento no índice temporário
            A[i], A[j] = A[j], A[i]
            # Avança o índice temporário
            i += 1

    # Troca o pivô com o elemento no índice final
    A[i], A[hi] = A[hi], A[i]
    return i  # Retorna o índice do pivô

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Array original:", arr)
    quicksort(arr, 0, len(arr) - 1)
    print("Array ordenado:", arr)
