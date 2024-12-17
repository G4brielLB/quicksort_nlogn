import numpy as np

N = [500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
# Gerar N números aleatórios entre 0 e 200.000
for n in N:
    numbers = np.random.randint(0, 200000, n)

    # Salvar no arquivo numbers.txt
    with open(f"numbers{n}.txt", "w") as f:
        for num in numbers:
            f.write(f"{num}\n")
