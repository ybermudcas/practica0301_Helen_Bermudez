import cProfile

def lectura_fichero(fichero1, fichero2):
    """Función que lee dos ficheros
    
    Parámetros:
        -Fichero1 = 50.csv
        -Fichero2 = 100.csv
        
    Salida:
        -Nombre capitalizado, DNI y letra de DNI
        """
    import csv
    with open(fichero1, "r") as file:
        lectura_documentos = csv.reader(file, delimiter= ',', quotechar= ',')
        for i in lectura_documentos:
            i[0] = nombre_capitalizado(i[0])
            print(i[0], i[1],calcular_letra(i[1]))
 
    with open(fichero2, "r") as file:
        lectura_documentos = csv.reader(file, delimiter= ',', quotechar= ',')
        for i in lectura_documentos:
            i[0] = nombre_capitalizado(i[0])
            print(i[0], i[1],calcular_letra(i[1]))

def nombre_capitalizado(nombre):
    """Función para poner nombre en formato capitalizado
    
    Parámetros:
        -nombre = nombre de usuario
        
    Salida:
        -Nombre de usuario en formato capitalizado
    """
    return nombre.upper()


def calcular_letra(DNI):
    """Función que calcula la letra de DNI
    
    Parámetros:
        -DNI = DNI ingresado para calcular
        
    Salida:
        -Letra de DNI"""
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    calcular = int(DNI) % 23
    letras = letras[calcular]
    return letras

lectura_fichero("50.csv", "1000.csv")

cProfile.run("lectura_fichero('50.csv', '1000.csv')")