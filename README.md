# quicksort_nlogn

Implementação do algoritmo de Quick Sort com as partições de Hoare e Lomuto e comparação com outros algoritmos de ordenação O(n log n), como Heapsort e Mergesort.

## Descrição

Este projeto tem como objetivo implementar e comparar diferentes variações do algoritmo de Quick Sort, especificamente as partições de Hoare e Lomuto, com outros algoritmos de ordenação que possuem complexidade O(n log n), como Heapsort e Mergesort.

## Algoritmos Implementados

- **Quick Sort com partição de Hoare**
- **Quick Sort com partição de Lomuto**
- **Heapsort**
- **Mergesort**

## Comparação

A comparação entre os algoritmos será feita com base em:

- Tempo de execução
- Número de comparações
- Número de trocas

## Como Executar

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/quicksort_nlogn.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd quicksort_nlogn
    ```
3. Execute o script `main.py`:
    ```sh
    python main.py
    ```

## O que o script `main.py` faz

O script `main.py` implementa os algoritmos de ordenação QuickSort (Hoare e Lamuto), Heapsort e Mergesort, que são algoritmos de ordenação com complexidade média de tempo O(n log n). Ele lê uma lista de números (N = [500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]), aplicando os algoritmos 5 vezes cada, salvando os resultados (individuais e gerais) em planilhas .xlsx com informações de cada tempo (ms), tempo médio (ms) e desvio padrão (ms).
## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

