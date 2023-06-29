import random
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_obstaculos):
    # Se inicializa una lista de contadores para cada contenedor
    contadores = [0] * (num_obstaculos + 1)
    
    # Se simula el recorrido de cada canica
    for _ in range(num_canicas):
        posicion = num_obstaculos // 2  # Se comienza en el contenedor central
        for _ in range(num_obstaculos):
            lado = random.choice([-1, 1])  # Se decide aleatoriamente si la canica cae a la izquierda (-1) o a la derecha (1)
            posicion += lado  # Se actualiza la posición de la canica en el contenedor
        contadores[posicion] += 1  # Se incrementa el contador del contenedor donde cayó la canica
    
    return contadores

def graficar_histograma(contadores):
    niveles = range(len(contadores))
    plt.bar(niveles, contadores)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Histograma de la Máquina de Galton')
    plt.show()

num_canicas = 3000
num_obstaculos = 12

resultados = simular_maquina_galton(num_canicas, num_obstaculos)
graficar_histograma(resultados)
