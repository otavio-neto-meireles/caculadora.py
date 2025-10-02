# Calculadora 

print (f"se atente-se que é uma caculadora seu cabaço, então coloca só numero e arrombado!")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
print(f"continuar caculando?")
    

 


print(f"Resultado é igual a {res}")