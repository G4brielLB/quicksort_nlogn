# Função para mesclar duas sublistas ordenadas
def merge(arr, left, mid, right):
    # Cria subarrays temporários
    L = arr[left:mid + 1]  # Subarray da esquerda
    R = arr[mid + 1:right + 1]  # Subarray da direita
    
    # Índices para percorrer as sublistas e o array original
    i, j, k = 0, 0, left
    
    # Combina os subarrays em ordem crescente
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copia os elementos restantes da sublista esquerda, se houver
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copia os elementos restantes da sublista direita, se houver
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Função principal do Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # Encontra o ponto médio
        
        # Aplica o Merge Sort recursivamente nas duas metades
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Mescla as duas metades ordenadas
        merge(arr, left, mid, right)


# Exemplo de uso
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Array original:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Array ordenado:", arr)
