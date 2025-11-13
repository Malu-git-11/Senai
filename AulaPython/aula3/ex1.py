
# Exercício 1
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if a > b:
    print(f"Maior: {a} Menor: {b}")
else:
    print(f"Maior: {b} Menor: {a}")


# Exercício 2
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# Exercíco 3
e = input("Digite seu estado civil (C/S/D/V/O): ")
if e == "C":
    print("C - Casado")
elif e == "S":
    print("S - Solteiro")
elif e == "D":
    print("D - Divorciado")
elif e == "V":
    print("V - Viúvo")
elif e == "O":
    print("O - Outros")
else:
    print("Opção inválida")
