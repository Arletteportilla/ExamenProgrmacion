"""Haz una tabla de multiplicar utilizando el ciclo for."""
for n in range(1, 12):
    for i in range(1, 11):
        print(n*i, end="\t")
    print("")