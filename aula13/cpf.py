def verificar_cpf(codigo_cpf):
    cpf_limpo = ''.join(filter(str.isdigit, codigo_cpf))

    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False

    soma, multiplicador = 0, 10
    for i in range(9):
        soma += int(cpf_limpo[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma, multiplicador = 0, 11
    for i in range(10):
        soma += int(cpf_limpo[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return digito1 == int(cpf_limpo[9]) and digito2 == int(cpf_limpo[10])


if __name__ == "__main__":
    codigo_cpf = input("Informe o CPF (XXX.XXX.XXX-XX): ")
    if verificar_cpf(codigo_cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")
