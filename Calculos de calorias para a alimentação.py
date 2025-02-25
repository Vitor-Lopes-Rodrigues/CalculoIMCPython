def calcular_tmb(peso, altura, idade):
    return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

def calcular_gcd(tmb, nivel_atividade):
    fatores_atividade = {
        "sedentario": 1.2,
        "levemente_ativo": 1.375,
        "moderadamente_ativo": 1.55,
        "muito_ativo": 1.725,
        "extremamente_ativo": 1.9
    }
    return tmb * fatores_atividade.get(nivel_atividade, 1.2)

def calcular_peso_maximo_imc(altura, imc_maximo=24.9):
    altura_m = altura / 100
    return imc_maximo * (altura_m ** 2)

def main():
    peso = float(input("Digite seu peso (kg) / Enter your weight (kg): "))
    altura = float(input("Digite sua altura (cm) / Enter your height (cm): "))
    idade = int(input("Digite sua idade / Enter your age: "))
    print("\nNíveis de atividade / Activity levels:")
    print("sedentario / sedentary")
    print("levemente_ativo / lightly active")
    print("moderadamente_ativo / moderately active")
    print("muito_ativo / very active")
    print("extremamente_ativo / extremely active")
    nivel_atividade = input("Escolha seu nível de atividade / Choose your activity level: ")
    
    tmb = calcular_tmb(peso, altura, idade)
    gcd = calcular_gcd(tmb, nivel_atividade)
    peso_maximo = calcular_peso_maximo_imc(altura)
    
    print(f"\nSua TMB é / Your BMR is: {tmb:.2f} kcal")
    print(f"Seu gasto calórico diário estimado é / Your estimated daily caloric expenditure is: {gcd:.2f} kcal")
    print(f"Peso máximo recomendado pelo IMC / Maximum recommended weight by BMI: {peso_maximo:.2f} kg")
    
    print("\nPara alcançar seus objetivos / To achieve your goals:")
    print(f"Manutenção de peso / Weight maintenance: {gcd:.2f} kcal/dia")
    print(f"Perda de peso (~500 kcal a menos) / Weight loss (~500 kcal deficit): {gcd - 500:.2f} kcal/dia")
    print(f"Ganho de peso (~500 kcal a mais) / Weight gain (~500 kcal surplus): {gcd + 500:.2f} kcal/dia")

if __name__ == "__main__":
    main()
