def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso / Underweight"
    elif 18.5 <= imc < 24.9:
        return "Peso normal / Normal weight"
    elif 25 <= imc < 29.9:
        return "Sobrepeso / Overweight"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1 / Obesity Grade 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2 / Obesity Grade 2"
    else:
        return "Obesidade Grau 3 / Obesity Grade 3"

def calcular_peso_minimo(altura):
    return 18.5 * (altura ** 2)

def calcular_peso_maximo(altura):
    return 24.9 * (altura ** 2)

peso = float(input("Digite seu peso em kg / Enter your weight in kg: "))
altura = float(input("Digite sua altura em metros / Enter your height in meters: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
peso_minimo = calcular_peso_minimo(altura)
peso_maximo = calcular_peso_maximo(altura)

print(f"Seu IMC é / Your BMI is: {imc:.2f}")
print(f"Classificação / Classification: {classificacao}")
print(f"Peso mínimo recomendado / Minimum recommended weight: {peso_minimo:.2f} kg")
print(f"Peso máximo recomendado / Maximum recommended weight: {peso_maximo:.2f} kg")