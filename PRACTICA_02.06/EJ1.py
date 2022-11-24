divisas= {"Euro":"€", "Dolar":"$", "Yen":"¥"}
pregunta = input("Introduce la divisa que quieras: ")
if pregunta in dict(divisas): print(divisas.get(pregunta.title()))
else:
    print("La moneda no está disponible")


