def número_entero(n):
    """Función que recibe un número entero positivo n y calcula el
    número de fibonacci asociado a ese número de manera recursiva.
    
    Parámetros:
        n = número estero positivo
        
    Salida:
        -Número de Fibonacci asociado a ese número de manera recursiva
        -El tiempo en que se ejecuta el código
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return número_entero(n-1) + número_entero(n-2)

import datetime
start_time = datetime.datetime.now()
print(número_entero(40))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es: ", end_time - start_time)


def número_bucle(n):
    """Función que recibe un número entero positivo n y calcula el
    número de fibonacci asociado a ese número en bucle.
    
    Parámetros:
        -n = número entero positivo
        
    Salida:
        -Número de Fibonacci asociado a ese número en bucle
        -El tiempo en que se ejecuta el código en bucle
    """
    x = 0
    y = 1
    for i in range(n-1):
        suma = x + y
        x = y
        y = suma
    return suma

import datetime
start_time_bucle = datetime.datetime.now()
print(número_bucle(40))
end_time_bucle = datetime.datetime.now()
print("El tiempo de ejecución es: ", end_time_bucle - start_time_bucle)