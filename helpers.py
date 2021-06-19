def celsius_to_kelvin (temperatura_celsius):
    """
    Função para converter temperatura celsius para kelvin
    :param temperatura_celcius:
    :return: temperatura em kelvin
    formula: c+273.15
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin

def celsius_to_fahreinheit (temperatura_celsius):
    """
       Função para converter temperatura celsius para fahreinheit
       :param temperatura_celcius:
       :return: temperatura em fahreinheit
       formula: (c * 9/5) + 32
       """
    temperatura_fahreinheit = (temperatura_celsius * 9/5) + 32
    return temperatura_fahreinheit