"""
Programa em python3
Conversor de temperatura
"""
from helpers import celsius_to_kelvin,celsius_to_fahreinheit

if __name__ == '__main__':
    while True:
        mensagem="\nDigite uma temperatura em Celsius"
        mensagem+="\nDigite 'q' para sair: "

        try:
            celsius = input(mensagem)
            if celsius.lower() != 'q':
                print(f"\nTemperatura em Kelvin(K)= {celsius_to_kelvin(float(celsius))}")
                print(f"Temperatura em Fahreiheit(F)= {celsius_to_fahreinheit(float(celsius))}")
            else:
                print("Até a próxima !")
                break
        except ValueError:
            print("Você digitou um caracter inválido.Digite 'q' para sair ou um novo valor !")