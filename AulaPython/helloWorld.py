"""
nome = input("Diga seu nome: ")
idade = input("Diga sua idade:")
anoAtual = 2025
anoNasc = (anoAtual - int(idade))

#Utilizando a vírgula para separar os valores na função print
print("Olá ",nome,", você tem ",idade," anos e nasceu em ",anoNasc,".")

#Utilizando a função f-string (formatação de strings)
print(f"Olá {nome}, você tem {idade} anos e nasceu em {anoNasc}.")
"""

#Teste de erro com condicional
if True:
    print("Isso vai dar errado!")
    