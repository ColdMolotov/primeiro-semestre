preco_roupa = float(input("Informe o preço da peça de roupa (em reais): "))

if preco_roupa > 5000:
    percentual_desconto = 0.3
elif preco_roupa >= 1001:
    percentual_desconto = 0.2
else:
    percentual_desconto = 0.1

preco_final = (1 - percentual_desconto) * preco_roupa

print(f"O preço original da roupa é R${preco_roupa:.2f}.")
print(f"Desconto aplicado: {percentual_desconto * 100}%.")
print(f"Valor do desconto: R${percentual_desconto * preco_roupa:.2f}.")
print(f"Preço final após desconto: R${preco_final:.2f}.")
