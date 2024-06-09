# 1
temp_celsius = float(input("Informe a temperatura em graus Celsius: "))
temp_fahrenheit = (9 * temp_celsius + 160) / 5
print(f"{temp_celsius}ºC equivale a {temp_fahrenheit}ºF.")

# 2
def celsius_para_fahrenheit(temp_c: float) -> float:
    temp_f = (9 * temp_c + 160) / 5
    print(f"{temp_c}ºC equivale a {temp_f}ºF.")
    return temp_f

temp_c = float(input("Informe a temperatura em graus Celsius: "))
celsius_para_fahrenheit(temp_c)

# 3
temperatura_f = float(input("Informe a temperatura em graus Fahrenheit: "))
temperatura_c = (5 * temperatura_f - 160) / 9
print(f"{temperatura_f}ºF equivale a {temperatura_c}ºC.")

# 4
def fahrenheit_para_celsius(temp_f: float) -> float:
    temp_c = (5 * temp_f - 160) / 9
    print(f"{temp_f}ºF equivale a {temp_c}ºC.")
    return temp_c

temp_f_in = float(input("Informe a temperatura em graus Fahrenheit: "))
fahrenheit_para_celsius(temp_f_in)
