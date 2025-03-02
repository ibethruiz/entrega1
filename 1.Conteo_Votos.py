import numpy as np

num_estu = 5000
num_candts = 30
candidatos = list(range(1, 31))

#random nos permite generar el numero del cadidato al que se votó de forma aleatoria del 1 al 30
votos = np.random.randint(1, 31, num_estu)

#lista en ceros para guardar los votos
list_votos= [0] * num_candts

for voto in votos:
    list_votos[voto-1] += 1

#ordenamiento (Método de burbuja)
for i in range(num_candts - 1):  
    for j in range(num_candts - 1 - i):  
        if list_votos[j] < list_votos[j + 1]:  #si el candidato actual tiene menos votos que el siguiente, intercambiamos
            #intercambiar votos
            list_votos[j], list_votos[j + 1] = list_votos[j + 1], list_votos[j]
            #intercambiar candidatos
            candidatos[j], candidatos[j + 1] = candidatos[j + 1], candidatos[j]

print("Candidato | Votos")
for i in range(num_candts):
    print(f"   {candidatos[i]:2d}     |  {list_votos[i]:4d}")










