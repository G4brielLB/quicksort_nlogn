import time

# Função para transformar o array em um Max-Heap
def heapify(arr, n, i):
    largest = i       # Inicializa o maior como a raiz
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2 # Índice do filho direito
    
    # Se o filho esquerdo é maior que a raiz
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Se o filho direito é maior que o maior até agora
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Se o maior não é a raiz, troca os elementos
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Heapify recursivamente no subárvore afetado
        heapify(arr, n, largest)


# Função principal do Heap Sort
def heap_sort(arr):
    n = len(arr)
    
    # Constrói o Max-Heap (reorganiza o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extrai elementos do heap um por um
    for i in range(n - 1, 0, -1):
        # Move a raiz atual (o maior elemento) para o final
        arr[i], arr[0] = arr[0], arr[i]
        
        # Chama heapify na subárvore reduzida
        heapify(arr, i, 0)


# Exemplo de uso
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Array original:", arr)
    heap_sort(arr)
    print("Array ordenado:", arr)
