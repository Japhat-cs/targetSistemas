# Função que inverte a string manualmente
def inverter_string(string):
    invertida = ""
    
    # Percorre a string de trás para frente e acumula os caracteres em 'invertida'
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

# Entrada da string 
entrada = "Quero entrar para a TargetSistemas."

# Chamando a função e exibindo a string invertida
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
