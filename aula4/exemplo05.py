# 1
ponto1_x = float(input("Informe o valor de x1: "))
ponto2_x = float(input("Informe o valor de x2: "))
ponto1_y = float(input("Informe o valor de y1: "))
ponto2_y = float(input("Informe o valor de y2: "))
diferenca_x = ponto2_x - ponto1_x
diferenca_y = ponto2_y - ponto1_y
distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5
print("A distância entre os pontos x e y é", distancia)
