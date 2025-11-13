#Exercício 1
nota = float(input("Digite a nota do aluno: "))

if nota < 7:
    print("Aluno reprovado.")
else:
    print("Aluno aprovado.")


#Exercício 2
idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade <= 11:
    print("Categoria: Infantil B")
elif 12 <= idade <= 13:
    print("Categoria: Juvenil A")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Idade fora das categorias.")


#Exercício 3
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")

if operacao == "soma":
    print("Resultado:", n1 + n2)
elif operacao == "subtracao":
    print("Resultado:", n1 - n2)
elif operacao == "multiplicacao":
    print("Resultado:", n1 * n2)
elif operacao == "divisao":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida.")
