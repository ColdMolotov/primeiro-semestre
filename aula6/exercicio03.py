from math import ceil

largura_aposento = float(input("Informe a largura do aposento, em metros: "))
comprimento_aposento = float(input("Informe o comprimento do aposento, em metros: "))
capacidade_lata = float(input("Informe a capacidade da lata de tinta em litros: "))
altura_parede = 2.8

area_total_paredes = (largura_aposento * altura_parede) * 2 + (comprimento_aposento * altura_parede) * 2  # são 4 paredes
area_porta_unica = 0.8 * 2.1
area_para_pintura = area_total_paredes - area_porta_unica  # descontando a área da porta
litros_necessarios = area_para_pintura / 3  # cada litro de tinta cobre 3m²
latas_necessarias = litros_necessarios / capacidade_lata

print(f"A área a ser pintada do aposento é de {area_para_pintura:.2f} m², sendo necessárias "
      f"{ceil(latas_necessarias)} latas de tinta para realizar a pintura das paredes.")
