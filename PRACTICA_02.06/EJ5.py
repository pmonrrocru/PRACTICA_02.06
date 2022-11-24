diccionario = {}
palabras = input("Introduce las traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(","):
    palabra, traduccion = i.split(":")
    diccionario[palabra] = traduccion

traducir = input("Introduce la frase que quieras traducir: ")
for i in traducir.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")


