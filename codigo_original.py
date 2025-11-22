import time

def es_primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    primos = []
    for num in range(1, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    inicio = time.time()
    limite = 100000 
    print(f"Calculando primos hasta {limite} (Versión Original)...")
    
    encontrar_primos(limite)
    
    fin = time.time()
    print(f"Tiempo de ejecución original: {fin - inicio:.4f} segundos")