#Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

# 1-Ya no sabemos cuantos clientes tendremos, 
# 2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
# 3-Lo mismo con la cantidad de puertas y los colores.
# 4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
# 5-Si la cantidad de clientes fue:
# --5.1: 0 a 5 personas no hay descuento
# --5.2: 6 a 10 personas: hay un descuento del 10%
# --5.3: 11 a 50 personas: hay un descuento del 15%
# --5.4: Más de 50 personas: El descuento es del 18%
# 6-Solo se va a mostrar que se vendió al final del programa


# B.-
# Creamos una función para calcular el precio.
def calcular_precio(marca,puertas,color,ventas):
    # Diccionario marcas
    marcas = {'FORD':100000,'CHEVROLET':120000,'FIAT':80000}       
    puertas = {2:50000,4:65000,5:78000}       
    colores = {'BLANCO':10000,'AZUL':20000,'NEGRO':30000} 
    # Suma los diccionarios
    precio = marcas[marca] + puertas[puerta] + colores[color]
    if ventas > 5 and ventas < 11:
        precio = precio * 0.9
    elif ventas > 10 and ventas < 51:
        precio = precio * 0.85
    elif ventas > 50:
        precio = precio * 0.82
    return precio 


# A.-
mas_clientes ='si'
# ventas es una lista, colección de ventas que se han generado.
ventas = []
# marcas es una lista
marcas = ['FORD','CHEVROLET','FIAT']
# puertas es una lista
puertas = [2,4,5]
# colores es una lista
colores = ['BLANCO','AZUL','NEGRO']

while mas_clientes == 'si':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    # Inicializo por default 
    marca = ''
    puerta = 0
    color = ''
    
    # Si el valor que tiene asignado la variable marca no es igual a algún elemento del diccionario marcas
    while marca not in marcas:
        marca = input('Ingrese marca: ')
        marca = marca.upper()
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de puertas: '))
    while color not in colores:
        color = input('Ingrese color: ')
        color = color.upper()

    # Agrego un elemento {en este caso un diccionario} a la lista ventas
    ventas.append({'nombre':nombre,'apellido':apellido,'marca':marca,'puertas':puerta,'color':color})
    # Si lo que se ingresa es diferente de si, es decir ya no se van a realizar mas ventas, termina el flujo.
    mas_clientes = input('Hay más clientes: ')
# Largo representa el nro. de elementos que tiene ventas, por ejemplo si se hicieron 3 ventas sería 3.
# Considerar, cada venta debe tener la información de cada cliente, por eso cada elemento de la lista
# ventas es una diccionario.
largo = len(ventas)
for i in ventas:
    precio = calcular_precio(marca,puertas,color,largo)
    # Imprimimos las ventas
    print("La persona: " + i['nombre'] + " " + i['apellido'] +
     " compro un auto marca " + i['marca'] + " de " + str(i['puertas']) + " puertas y color " + i['color'] +
      " con un precio final de S/. " + str(precio))

# Existe un defecto, cuando se realiza mas de una venta, el precio que se muestra es el de la última venta.
# por ejemplo:
# Descripción venta 1 precio3
# Descripción venta 2 precio3
# Descripción venta 3 precio3







