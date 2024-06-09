# 1
print("Por favor, insira os valores do Retângulo...")
base_ret = int(input("Valor da base: "))
altura_ret = int(input("Valor da altura: "))
area_ret = base_ret * altura_ret
print("Base:", base_ret, " Altura:", altura_ret, " Área:", area_ret)


def calcular_area(base: float, altura: float) -> float:
    area = base * altura
    print(f"Um retângulo com base {base} e altura {altura} possui área de {area}.")
    return area

print("Informe as dimensões do retângulo.")
base_input = float(input("Digite o valor da base: "))
altura_input = float(input("Digite o valor da altura: "))
calcular_area(base_input, altura_input)
