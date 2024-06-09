salario = float(input("Digite seu salário: "))
aumento = float(input("Digite o aumento em %: "))
print(f"O salário {int(salario)} com {int(aumento)}% de aumento equivale a {int((1 + aumento / 100) * salario)}.")