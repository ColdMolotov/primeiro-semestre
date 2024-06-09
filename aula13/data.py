from datetime import datetime, date

def verificar_idade(data_nascimento):
    try:
        data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = date.today()
        anos = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return anos >= 18
    except ValueError:
        return False

if __name__ == "__main__":
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    if verificar_idade(nascimento):
        print("Maior de idade!")
    else:
        print("Data inválida ou menor de 18 anos.")
