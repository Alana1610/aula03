nome = input("escreva seu nome")
idade = int (input ("escreva sua idade"))
salario = float (input("escreva seu salario"))
percentual = int (input("quantos % de aumento do salario"))

aumento = (salario * percentual ) / 100
novoSalario = aumento + salario

print(f"seu nome e {nome} sua idade e {idade} seu salario anterior era {salario}, com aumento {percentual} (em reais {aumento}) seu salario atual é de {novoSalario}")
