productos= {"pan":1.40, "huevos":2.30, "cebolla":0.85, "aceite":4.35}
articulo = input("Introduce el artículo que quieras: ")
if articulo in productos:
   cantidad = float(input("Introduce la cantidad del articulo: "))
   print(cantidad * productos.get(articulo), "€")
else:
   print("El artículo elegido no está disponible.")