def invertirDic(dic):
    diccionario = {val:clave for clave,val in dic.items()}
    return diccionario

diccionario = {"Valor1": 0, "Valor2": 1, "Valor": 2}
diccInvertido = invertirDic(diccionario)
print(f'Diccionario original: {diccionario}\nDiccionario invertido{diccionario}')