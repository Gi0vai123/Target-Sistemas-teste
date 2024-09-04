def inverter_string(s):
    lista_caracteres = list(s)
    
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        
        
        inicio += 1
        fim -= 1
    
    return ''.join(lista_caracteres)

entrada = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(entrada))
