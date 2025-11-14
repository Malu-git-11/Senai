#Exercício 1
nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido. A nota deve estar entre 0 e 10.")
    nota = float(input("Digite novamente: "))

print(f"Nota válida: {nota}")

#Exercício 2
quant = int(input("Quantas notas você vai inserir? "))

soma = 0

for i in range(quant):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota

media = soma / quant

print(f"A média aritmética é: {media}")

#Exercício 3
qtdTurmas = int(input("Quantas turmas? "))

somaAlunos = 0

for i in range(qtdTurmas):
    alunos = int(input(f"Quantidade de alunos da turma {i+1}: "))

    while alunos > 40:
        print("Máximo permitido é 40 alunos.")
        alunos = int(input(f"Informe novamente a quantidade de alunos da turma {i+1}: "))

    somaAlunos += alunos

media = somaAlunos / qtdTurmas
print(f"Média de alunos por turma: {media}")

#Exercício 4
numero = input("Digite um número: ")

quantidade = len(numero)

print(f"Quantidade de dígitos: {quantidade}")

#Exercício 5
senha = input("Crie uma senha: ")

confirmacao = input("Digite a senha novamente: ")

while confirmacao != senha:
    print("Senhas não correspondem.")
    confirmacao = input("Digite novamente: ")

print("Senha confirmada com sucesso!")

#Exercício 6
soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para parar): "))

print(f"Soma total: {soma}")