import re

print("Bem vindo ao conversor de Temperatura!!!")

while True: #Loop para poder continuar o programa
    temperatura = input("Digite a temperatura com a letra da medida(ex: 34ºC): ") #Recebe o dado à ser fatiado
    transf = input("Quer tranformar para qual medida?\n") #Recebe a medida de destino

    resultado = re.match(r"(\d+)(º|°)([C|c|Celsius|celsius|F|f|Fahrenheit|fahrenheit|K|k|Kelvin|kelvin])", temperatura) #Fatiamento do dado

    if resultado:
        numero = float(resultado.group(1))  # Captura a parte numérica
        simbolo = resultado.group(2)  # Captura a sinal
        unidade = (resultado.group(3))  # Captura a unidade (caracteres não numéricos)

        match unidade:
            case ('C'|'c'|'Celsius'|'celsius'): # Se a unidade for Celsius  
                match transf:
                    case ('C'|'c'|'Celsius'|'celsius'):
                        print(f"{temperatura} em Celsius é {temperatura}")
                    case ('F'|'f'|'Fahrenheit'|'fahrenheit'):
                        print(f"{temperatura} em Fahrenheit é {(numero*1.8)+32}{simbolo}F")
                    case ('K'|'k'|'Kelvin'|'kelvin'):
                        print(f"{temperatura} em Kelvin é {numero+273.15}{simbolo}K")
                    case _:
                        print("Unidade não suportada")
            case ('F'|'f'|'Fahrenheit'|'fahrenheit'): # Se a unidade for Fahrenheit
                match transf:
                    case ('C'|'c'|'Celsius'|'celsius'):
                        print(f"{temperatura} em Celsius é {(numero-32)/1.8}{simbolo}C")
                    case ('F'|'f'|'Fahrenheit'|'fahrenheit'):
                        print(f"{temperatura} em Fahrenheit é {temperatura}")
                    case ('K'|'k'|'Kelvin'|'kelvin'):
                        print(f"{temperatura} em Kelvin é {(numero-32)/1.8+273.15}{simbolo}K")
                    case _:
                        print("Unidade não suportada")
            case ('K'|'k'|'Kelvin'|'kelvin'): # Se a unidade for Kelvin
                match transf:
                    case ('C'|'c'|'Celsius'|'celsius'):
                        print(f"{temperatura} em Celsius é {numero-273.15}{simbolo}C")
                    case ('F'|'f'|'Fahrenheit'|'fahrenheit'):
                        print(f"{temperatura} em Fahrenheit é {(numero-273.15)*1.8+32}{simbolo}F")
                    case ('K'|'k'|'Kelvin'|'kelvin'):
                        print(f"{temperatura} em Kelvin é {temperatura}")
                    case _:
                        print("Unidade não suportada")
            case _:
                print("Unidade não suportada") 
    else:
        print("Formato de temperatura inválido. Por favor, tente novamente.")
    continuar = input("Deseja converter outra temperatura? (s/n): ")
    if continuar.lower() not in ['s', 'S', 'sim', 'Sim', 'SIM']:
        print("Obrigado por usar o conversor de Temperatura!")
        break