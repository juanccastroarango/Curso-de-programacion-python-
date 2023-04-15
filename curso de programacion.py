nombredelvendedor=input("Digite el nombre del vendedor:")
salario=float(input("Digite el salario:"))
venta1=float(input("Digite el valor de la venta 1:"))
venta2=float(input("Digite el valor de la venta 2:"))
venta3=float(input("Digite el valor de la venta 3:"))
gananciasporventa=venta1+venta2+venta3
gananciadeventa=gananciasporventa *0.10
gananciaporventa= round((gananciasporventa))
print (f"la ganancia es={gananciadeventa}")
print("Sueldo a consignar:")
print(salario+gananciadeventa)

nombredelatienda=("Tienda solo gamers")
print(nombredelatienda.center(30))
videojuego=float(input("Ingrese el valor del juego:"))
descuento1=videojuego *0.15
descuento=round((descuento1))
print(f"el descuento es={descuento1}")
print("Total a pagar")
pagototal=videojuego-descuento1
print(pagototal)

universidad=("Bienvenido al CET de colsubsidio")
print(universidad.center(44))
nombredelalumno=input("Digite el nombre del alumno:")
materia=("Fundamentos de programacion")
input("Digite la materia:")
calificacion1=float(input("Digite la calificacion1:")) 
calificacion2=float(input("Digite la calificacion2:")) 
calificacion3=float(input("Digite la calificacion3:")) 
promedio=round((calificacion1+calificacion2+calificacion3) / 3,2)
print(f"Calificacion final es={promedio}")

empresa=("Bienvenido a Thomas Mti")
print(empresa.center(35))
nombredelempleado=input("Digite el nombre del empleado:")
edaddelempleado=int(input("Digite la edad del empleado:"))
if edaddelempleado >=55:
  print("Aplica al bono del 5%")
else:
  print("No aplica al bono del 5%")
salariodelempleado=int(input("Digite el salario:"))
if salariodelempleado < 1000000:
  print("Tiene derecho al 2 porciento sobre su sueldo")
else:
  print("No tiene derecho al 2 porciento sobre su sueldo")
diaslaborados=int(input("Digite los dias laborados:"))
if diaslaborados >=20:
   print("Tiene derecho al bono de alimentacion")
else:
   print("No tiene derecho al bono de alimentacion")
estadocivil=input("Usted es casado?:")
hijos=input("Usted tiene hijos?:")
hijos2=int(input("Cuantos hijos tiene?:"))
if hijos2 > 0 :
   print("Tiene derecho al paseo")
else:
   print("No tiene derecho al paseo")
print("¡Gracias por su Tiempo,hasta pronto!")




