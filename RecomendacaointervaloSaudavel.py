def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"  # Below weight
    elif 18.5 <= imc < 24.9:
        return "Peso normal"  # Normal weight
    elif 25 <= imc < 29.9:
        return "Sobrepeso"  # Overweight
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"  # Obesity Grade 1
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"  # Obesity Grade 2
    else:
        return "Obesidade Grau 3"  # Obesity Grade 3

def calcular_peso_minimo(altura):
    return 18.5 * (altura ** 2)

def calcular_peso_maximo(altura):
    return 24.9 * (altura ** 2)

def recomendar_calorias(imc, peso, altura):
    calorias_bmr = 25 * peso  # Basal metabolic rate (calorias básicas para manutenção)

    if imc < 18.5:
        calorias_recomendadas = calorias_bmr + 200  # For underweight
        recomendacao = "Para ganhar peso / To gain weight"
    elif 18.5 <= imc < 24.9:
        calorias_recomendadas = calorias_bmr  # For normal weight
        recomendacao = "Para manutenção do peso / To maintain weight"
    elif 25 <= imc < 29.9:
        calorias_recomendadas = calorias_bmr - 200  # For overweight
        recomendacao = "Para perder peso / To lose weight"
    else:
        calorias_recomendadas = calorias_bmr - 400  # For obesity
        recomendacao = "Para perder peso de forma significativa / To lose significant weight"

    return calorias_recomendadas, recomendacao

peso = float(input("Digite seu peso em kg: / Enter your weight in kg: "))
altura = float(input("Digite sua altura em metros: / Enter your height in meters: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
peso_minimo = calcular_peso_minimo(altura)
peso_maximo = calcular_peso_maximo(altura)
calorias_recomendadas, recomendacao = recomendar_calorias(imc, peso, altura)

print(f"Seu IMC é: {imc:.2f} / Your BMI is: {imc:.2f}")
print(f"Classificação: {classificacao} / Classification: {classificacao}")
print(f"Peso mínimo recomendado: {peso_minimo:.2f} kg / Recommended minimum weight: {peso_minimo:.2f} kg")
print(f"Peso máximo recomendado: {peso_maximo:.2f} kg / Recommended maximum weight: {peso_maximo:.2f} kg")
print(f"Calorias recomendadas por dia: {calorias_recomendadas:.0f} kcal ({recomendacao}) / Recommended daily calories: {calorias_recomendadas:.0f} kcal ({recomendacao})")
