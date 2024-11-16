import re

print("Bem vindo ao conversor de Temperatura!!!")

temperatura = input("Digite a temperatura com a letra da medida(ex: 34ºC): ")

resultado = re.match(r"(\d+)(\D+)", temperatura)

numero = resultado.group(1)  # Captura a parte numérica
unidade = resultado.group(2)  # Captura a unidade (caracteres não numéricos)

match unidade:
    case unidade ('ºC'|'ºc'|'ºCelsius'|'ºcelsius'):
    case unidade ('ºF'|'ºf'|'ºFahrenheit'|'ºfahrenheit'):
    case unidade ('ºK'|'ºk'|'ºKelvin'|'ºkelvin'):
    case unidade _: