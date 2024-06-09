primos_encontrados = ()
numero = 100

while len(primos_encontrados) < 10:
    for divisor in range(2, numero):
        if divisor == numero - 1:
            primos_encontrados += (numero,)
            numero += 1
            break
        if numero % divisor == 0:
            numero += 1
            break
    else:
        numero += 1

print(primos_encontrados)
