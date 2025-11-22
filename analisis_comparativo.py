import cProfile
import pstats
import time
import matplotlib.pyplot as plt
import numpy as np
from codigo_original import encontrar_primos 
from codigo_optimizado import encontrar_primos_list, encontrar_primos_numpy

def perfilar_funcion(funcion, arg, nombre_archivo):#ejecutamos cprofile sobre una funcion y guardamos los resultados
    profiler = cProfile.Profile()
    profiler.enable()
    funcion(arg)
    profiler.disable()
    
    with open(nombre_archivo, 'w') as f: #guardamos los resultados en un archivo
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('cumtime')
        stats.print_stats()
    return stats

if __name__ == "__main__":
    RANGO = 100000 
    
    print(f"--- Iniciando Profiling (N={RANGO}) ---")
    
    print("Ejecutando Original...")#medimos el tiempo de ejecucion del original
    start = time.time()
    perfilar_funcion(encontrar_primos, RANGO, 'profiling_original.txt')
    tiempo_original = time.time() - start
    print(f"Original: {tiempo_original:.4f} s")

  
    print("Ejecutando Optimizado (List)...") #medimos el tiempo del optimizado con listas
    start = time.time()
    perfilar_funcion(encontrar_primos_list, RANGO, 'profiling_opt_python.txt')
    tiempo_opt_py = time.time() - start
    print(f"Optimizado (List): {tiempo_opt_py:.4f} s")

   
    print("Ejecutando NumPy...") #medimos el tiempo del optimizado con numpy
    start = time.time()
    perfilar_funcion(encontrar_primos_numpy, RANGO, 'profiling_opt_numpy.txt')
    tiempo_numpy = time.time() - start
    print(f"NumPy: {tiempo_numpy:.4f} s")

    #graficos
    etiquetas = ['Original', 'Optimizado (List)', 'NumPy']
    tiempos = [tiempo_original, tiempo_opt_py, tiempo_numpy]
    
    colores = ['red', 'blue', 'green']
    
    plt.figure(figsize=(10, 6))
    barras = plt.bar(etiquetas, tiempos, color=colores)
    
    plt.ylabel('Tiempo (segundos)')
    plt.title(f'Comparativa de Tiempos de Ejecución (N={RANGO})')
    
    for barra in barras:
        yval = barra.get_height()
        if yval > 0:
            plt.text(barra.get_x() + barra.get_width()/2, yval, f'{yval:.4f}s', 
                     ha='center', va='bottom')
                 
    plt.savefig('comparativa_tiempos.png')
    plt.show()