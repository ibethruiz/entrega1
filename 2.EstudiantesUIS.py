import numpy as np

carreras = {
    11: "Ing de Sistemas",
    21: "Ing Civil",
    27: "Diseño Industrial",
    30: "Lic en Música"}

num_estudiantes = 7

codigos = np.array([101, 102, 103, 114, 105, 116, 107])
nombres = np.array(["Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4", "Estudiante 5", "Estudiante 6", "Estudiante 7"])
carreras_estudiantes = np.array([11, 11, 21, 21, 27, 27, 30])  # Códigos de carrera
promedios = np.array([4.2, 3.8, 4.5, 4.0, 3.5, 4.7, 4.0])
fecha_ingreso = np.array([1985, 1992, 1988, 2000, 1985, 2015, 1987])




codigo_carrera = int(input("Ingrese el código de la carrera (11, 21, 27, 30): "))

if codigo_carrera in carreras:
    print( f"\nEstudiantes de {carreras[codigo_carrera]}")
    print(f"\nEstudiantes con promedio mayor o igual a 4 ")
    print("Código  | Nombre")
    j = 0  #contador de estudiantes

    for i in range(num_estudiantes): 
        if carreras_estudiantes[i] == codigo_carrera and promedios[i] >= 4:
            print(f"{codigos[i]:6d} | {nombres[i]}")
            j += 1   

    print(f"\nTotal de estudiantes encontrados: {j}")
else:
     print("Código de carrera no disponible o no existe.")


#Estudiantes condicionales
#Verificar si un estidiante esta condicional
condicional = np.zeros(num_estudiantes)  
for i in range(num_estudiantes):
    if promedios[i] <= 3.2:  #si el promedio es menor o igual a 3.2, es estudiante está condicional
        condicional[i] = True


print("\nEstudiantes condicionales (promedio menor o igual a 3.2)")
print("Código  | Nombre  ")

for i in range(num_estudiantes):
    if carreras_estudiantes[i] == codigo_carrera and promedios[i] < 3.2:
        print(f"{codigos[i]:6d} | {nombres[i]} ")

#Estudiantes que ingresaron antes de 1990
print("\nEstudiantes que ingresaron antes de 1990")
print("Código  | Nombre  ")

for i in range(num_estudiantes):  
    if carreras_estudiantes[i] == codigo_carrera and fecha_ingreso[i] < 1990: 
        print(f"{codigos[i]:6d} | {nombres[i]}")