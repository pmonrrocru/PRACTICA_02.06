nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de móvil: ")

datos= {"nombre":nombre, "edad":edad, "direccion":direccion, "telefono":telefono}
print(nombre + " tiene " + edad + " años" + ", vive en " + direccion + " y su número de telefono es " + telefono)