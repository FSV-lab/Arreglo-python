frutas = ["manzana","pera","piña","banano","naranja"]
cantidad_frutas  = len(frutas)
print("la lista contiene",cantidad_frutas,"frutas.")

#agregando un elementos a la lista
frutas.append("Uva")
print("Agregaste una nueva fruta a la canasta",frutas)

#revisando la lista despues de agregar a la lista

print("La lista despues de agregar una nueva fruta es: ",frutas)

#eliminando un elemento de la lista

frutas.remove("banano")
print("Eliminaste una fruta de la canasta",frutas)
