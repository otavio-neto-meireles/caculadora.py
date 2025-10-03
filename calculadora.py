# Calculadora 

#olhar o caderno para explixar.
def validar_float(entrada):
    try:
        return float(entrada)
    except ValueError:
        return False

print("Atente-se que é uma calculadora, seu cabaço, então coloca só número, o vacilão! 😎")

#usei i while para criar o loop mass detalhes no caderno while True
while True:

    while True:
        entrada_num1 = input("Digite o primeiro número: ")
        num1 = validar_float(entrada_num1)
        if num1 is not False:  # is not false = checa se o valor não é falso. MAS nao posso usar o IF no python (olharrr o caderno)
            break #usado para quebrar o loop do while se float for verdaderio(olhar o caderno)
        else:# SE conersão falhar é usada para mostrar o print print("Entrada inválida. Por favor, digite um número.")
            print("Entrada inválida. Por favor, digite um número.")


    while True:
        entrada_num2 = input("Digite o segundo número: ")
        num2 = validar_float(entrada_num2)
        if num2 is not False:
            break
        else:
            print("Entrada inválida. Por favor, digite um número.")

 
    operacao = input("Digite a operação (+, -, *, /): ")
    res = None  # é usado qundo voce quer criar uma variavel e nao tem um valor, como se tivesse preparando o espaço

   
    match operacao:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "*":
            res = num1 * num2
        case "/":
            if num2 != 0:
                res = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida, não foi na aula de matemática do fundamental né 😅")
        case _:
            print("Operação não reconhecida. Aprende a calcular primeiro 😎")


    if res is not None:
        print(f"💥 O Resultado é igual a {res}")

   
    retry = input("Deseja tentar novamente? (s/n): ").lower() #usei para que o input aceitasse qualquer variação na letra.
    if retry == "s":
        print("Bora lá, seu gênio! 🧠💪")
    elif retry == "n":
        print("Valeu, vacilão! Encerrando a calculadora 😎👋")
        break
    else:
        print("Responde direito, cabaço! Vou encerrar por segurança 😅")
        break
