import numpy as np

def es_primo_opt(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    limite_raiz = int(n**0.5) + 1
    for i in range(3, limite_raiz, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_list(limite):
    return [num for num in range(1, limite + 1) if es_primo_opt(num)]

def encontrar_primos_numpy(limite):
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False # 0 y 1 no son primos
    
    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            es_primo[i*i : limite+1 : i] = False
            
    return np.nonzero(es_primo)[0]