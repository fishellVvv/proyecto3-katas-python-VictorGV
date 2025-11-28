from functools import reduce

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías en kata10_media_segura."""
    pass

# PROYECTO 3 - Katas Python
# Este tercer proyecto consiste en completar, validar y entregar todos los ejercicios de Python que se plantean a continuación:


def kata01_frecuencia_letras(texto):
    """
    Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
    """
    # Diccionario donde acumulamos las apariciones de cada carácter
    frecuencias = {}
    # Recorremos el texto carácter a carácter, ignorando los espacios
    for c in texto:
        if c != " ":
            # Usamos dict.get para sumar 1 (0 por defecto si la clave no existe aún)
            frecuencias[c] = frecuencias.get(c, 0) + 1
    return frecuencias


def kata02_duplicar_lista(numeros):
    """
    Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
    """
    # Aplicamos una función lambda a cada número con map para duplicar su valor
    return list(map(lambda num: num * 2, numeros))


def kata03_encontrar_coincidentes(palabras, objetivo):
    """
    Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
    """
    # Quitamos espacios y pasamos a minúsculas
    objetivo_limpio = objetivo.strip().lower()
    # Si el objetivo queda vacío, devolvemos lista vacía
    if not objetivo_limpio:
        return []
    # Usamos filter + lambda para quedarnos solo con las palabras que contienen el objetivo
    return list(filter(lambda p: objetivo_limpio in p.lower(), palabras))


def kata04_diferencia_listas(lista1, lista2):
    """
    Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
    """
    # Usamos map con dos listas en paralelo: restamos cada par de elementos
    return list(map(lambda num_l1, num_l2: num_l1 - num_l2, lista1, lista2))


def kata05_media_con_estado(notas, nota_aprobado=5):
    """
    Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
    """
    # Si no hay notas la media es 0
    if not notas:
        return 0, "suspenso"
    # Calculamos la media de la lista de números
    nota_media = sum(notas) / len(notas)
    # Decidimos el estado
    estado = "aprobado" if nota_media >= nota_aprobado else "suspenso"
    # Devolvemos la tupla
    return nota_media, estado


def kata06_factorial_recursivo(num):
    """
    Escribe una función que calcule el factorial de un número de manera recursiva.
    """
    # No existe el factorial de números negativos
    if num < 0:
        raise ValueError("El factorial no está definido para números negativos")
    # El factorial de 0 y 1 es 1
    elif num <= 1:
        return 1
    # Usamos la recursividad para ir multiplicando por cada iteración de num - 1
    return num * kata06_factorial_recursivo(num - 1)


def kata07_tuplas_a_strings(lista_tuplas):
    """
    Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
    """
    # Convertimos cada elemento de la tupla a str y los unimos con '-' usando el método join
    return list(map(lambda tupla: "-".join(map(str, tupla)), lista_tuplas))


def kata08_division_segura():
    """
    Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
    """
    dividendo = input("Introduce el dividendo: ")
    divisor = input("Introduce el divisor: ")
    try:
        # Intentamos convertir a float y realizar la división
        dividendo = float(dividendo)
        divisor = float(divisor)
        resultado = dividendo / divisor
    except ValueError:
        # Alguno de los valores no es numérico
        print(f"La división '{dividendo} / {divisor}' no fue exitosa, los valores deben ser numéricos")
    except ZeroDivisionError:
        # El divisor es cero
        print(f"La división '{dividendo} / {divisor}' no fue exitosa, no se puede dividir entre cero")
    else:
        # Si no ha habido ninguna excepción nos da la respuesta exitosa
        print(f"La división '{dividendo} / {divisor} = {resultado}' fue exitosa")


def kata09_filtrar_mascotas(nombres_mascotas):
    """
    Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Usamos filter + lambda para quedarnos solo con las mascotas cuyo nombre (normalizado con title()) no está en la lista de prohibidas
    return list(filter(lambda mascota: mascota.title() not in mascotas_prohibidas, nombres_mascotas))


def kata10_media_segura(numeros):
    """
    Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
    """
    if not numeros:
        # Si la lista está vacía lanzamos excepción personalizada
        raise ListaVaciaError("La lista de números está vacía")
    # Calculamos la media de la lista de números
    return sum(numeros) / len(numeros)
    

def kata11_pedir_edad():
    """
    Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
    """
    edad = input("Indica tu edad: ")
    try:
        edad = int(edad)
        if edad < 0 or edad > 120:
            # Forzamos un ValueError si la edad está fuera del rango esperado
            raise ValueError("Edad fuera de rango (0-120)")
    except ValueError:
        # Cualquier problema de conversión o rango se maneja aquí
        print("Error: introduce una edad numérica entre 0 y 120.")
    else:
        # Si no ha habido ninguna excepción te escribe un mensaje
        print(f"Tu edad es {edad}, ¡estás en tu mejor momento!")


def kata12_longitudes_palabras(frase):
    """
    Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
    """
    # Separamos la frase por espacios
    palabras = frase.split()
    # Aplicamos len a cada palabra con map para calcular su longitud
    return list(map(len, palabras))


def kata13_mayuscula_minuscula(caracteres):
    """
    Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
    """
    # pasamos los caracteres a una lista ordenada sin repeticiones
    caracteres_unicos = []
    for c in caracteres:
        if c.lower() not in caracteres_unicos:
            caracteres_unicos.append(c.lower())
    # Transformamos cada carácter en una tupla (MAY, min)
    return list(map(lambda ch: (ch.upper(), ch.lower()), caracteres_unicos))
    

def kata14_palabras_que_empiezan_por(palabras, letra):
    """
    Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
    """
    # Nos quedamos con las palabras que empiezan por la letra ignorando mayúsculas (y evitando error si la palabra está vacía)
    return list(filter(lambda palabra: palabra != "" and palabra[0].lower() == letra.lower() , palabras))


def kata15_sumar_tres_lambda(numeros):
    """
    Crea una función lambda que sume 3 a cada número de una lista dada.
    """
    # Aplicamos una función lambda a cada número con map para sumar 3
    return list(map(lambda num: num + 3, numeros))


def kata16_palabras_mas_largas_que(frase, n):
    """
    Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
    """
    # Separamos la frase por espacios
    palabras = frase.split()
    # Aplicamos una función lambda a cada palabra para comparar su longitud con n
    return list(filter(lambda palabra: len(palabra) > n, palabras))


def kata17_digitos_a_numero(digitos):
    """
    Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
    """
    # En cada iteración multiplicamos por 10 y le sumamos el siguiente dígito (comenzando por 0)
    return reduce(lambda acumulador, num: (acumulador * 10) + num, digitos, 0)


def kata18_filtrar_mejores_estudiantes(nota_corte=90):
    """
    Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
    """
    estudiantes = [
        {"nombre": "Pepe", "edad": 25, "calificacion": 90},
        {"nombre": "Luisa", "edad": 20, "calificacion": 96},
        {"nombre": "Andrés", "edad": 31, "calificacion": 78},
    ]
    # Comparamos la calificación para comprobar que sea >= que la nota de corte (por defecto 90)
    return list(filter(lambda estudiante: estudiante["calificacion"] >= nota_corte, estudiantes))


def kata19_filtrar_impares_lambda(numeros):
    """
    Crea una función lambda que filtre los números impares de una lista dada.
    """
    # Aplicamos una función lambda a cada número para comprobar si es impar
    return list(filter(lambda num: num % 2 != 0, numeros))


def kata20_filtrar_enteros(valores):
    """
    Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
    """
    # con type() comprobamos si cada valor es int
    return list(filter(lambda valor: type(valor) is int, valores))


def kata21_cubo_lambda(num):
    """
    Crea una función que calcule el cubo de un número dado mediante una función lambda.
    """
    # definimos la función cubo con lambda
    cubo = lambda n: n ** 3
    return cubo(num)


def kata22_producto_lista(numeros):
    """
    Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
    """
    # En cada iteración multiplicamos al acumulador (comenzando por 1)
    return reduce(lambda acumulador, num: acumulador * num, numeros, 1)


def kata23_concatenar_palabras(palabras):
    """
    Concatena una lista de palabras. Usa la función reduce().
    """
    # Controlamos el caso de que la lista esté vacía y concatenamos con "_"
    return reduce(lambda acumulador, palabra: palabra if acumulador == "" else acumulador + "_" + palabra, palabras, "")

def kata24_diferencia_total(numeros):
    """
    Calcula la diferencia total en los valores de una lista. Usa la función reduce().
    """
    # En cada iteración restamos al acumulador
    return reduce(lambda acumulador, num: acumulador - num, numeros)


def kata25_contar_caracteres(texto):
    """
    Crea una función que cuente el número de caracteres en una cadena de texto dada.
    """
    # básicamente un len()... (espero que el objetivo de la kata no fuese hacer un for in)
    return len(texto)


def kata26_modulo_lambda(dividendo, divisor):
    """
    Crea una función lambda que calcule el resto de la división entre dos números dados.
    """
    # definimos la función módulo con lambda
    modulo = lambda num1, num2: num1 % num2
    return modulo(dividendo, divisor)


def kata27_promedio(numeros):
    """
    Crea una función que calcule el promedio de una lista de números.
    """
    pass


def kata28_primer_duplicado(elementos):
    """
    Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
    """
    pass


def kata29_enmascarar(valor):
    """
    Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
    """
    pass


def kata30_son_anagramas(palabra1, palabra2):
    """
    Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
    """
    pass


def kata31_buscar_nombre():
    """
    Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
    """
    pass


def kata32_buscar_puesto_empleado(nombre_completo, empleados):
    """
    Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
    """
    pass


def kata33_sumar_listas_lambda(lista1, lista2):
    """
    Crea una función lambda que sume elementos correspondientes de dos listas dadas.
    """
    pass


class Arbol:
    """
    Kata 34: Crea la clase Arbol
     · Define un árbol genérico con un tronco y ramas como atributos.
     · Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.

     · Código a seguir:
      a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
      b. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
      c. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
      d. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
      e. Implementar el método quitar_rama para eliminar una rama en una posición específica.
      f. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

     · Caso de uso:
      a. Crear un árbol.
      b. Hacer crecer el tronco una unidad.
      c. Añadir una nueva rama.
      d. Hacer crecer todas las ramas una unidad.
      e. Añadir dos nuevas ramas.
      f. Retirar la rama situada en la posición 2.
      g. Obtener información sobre el árbol.
    """

    def __init__(self):
        pass

    def crecer_tronco(self):
        pass

    def nueva_rama(self):
        pass

    def crecer_ramas(self):
        pass

    def quitar_rama(self, posicion):
        pass

    def info_arbol(self):
        pass


class UsuarioBanco:
    """
    Kata 35: Crea la clase UsuarioBanco
     · Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
     · Métodos: retirar_dinero, transferir_dinero, agregar_dinero.

     · Código a seguir:
      a. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
      b. Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
      c. Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
      d. Implementar agregar_dinero para aumentar el saldo del usuario.

     · Caso de uso:
      a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
      b. Agregar 20 unidades al saldo de Bob.
      c. Transferir 80 unidades de Bob a Alicia.
      d. Retirar 50 unidades del saldo de Alicia.
    """

    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        pass

    def retirar_dinero(self, cantidad):
        pass

    def transferir_dinero(self, otro_usuario, cantidad):
        pass

    def agregar_dinero(self, cantidad):
        pass


def contar_palabras(texto):
    """
    -> Kata 36: Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
    """
    pass


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    -> Kata 36: Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
    """
    pass


def eliminar_palabra(texto, palabra):
    """
    -> Kata 36: Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
    """
    pass


def procesar_texto(texto, opcion, *args):
    """
    Kata 36: Crea una función llamada procesar_texto
     · Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
     · Código a seguir:
      a. Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
      b. Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
      c. Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
      d. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
     · Caso de uso:
      a. Verificar el funcionamiento completo de procesar_texto.
    """
    pass


def kata37_momento_del_dia():
    """
    Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
    """
    pass


def kata38_nota_a_texto(nota):
    """
    Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
     · Reglas:
       0 - 69:  insuficiente
      70 - 79:  bien
      80 - 89:  muy bien
      90 - 100: excelente
    """
    pass


def kata39_area(figura, datos):
    """
    Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
    """
    pass


def kata40_descuento_tienda_online():
    """
    Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
      a. Solicitar al usuario el precio original de un artículo.
      b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
      c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
      d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
      e. Mostrar el precio final de la compra, considerando o no el descuento.
      f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
    """
    pass


if __name__ == "__main__":

    # Pruebas manuales de las katas

    print("\n=== Kata 01 - frecuencia letras ===")
    texto = "Python mola"
    print(f"'{texto}' => {kata01_frecuencia_letras(texto)}")

    print("\n=== Kata 02 - duplicar lista ===")
    numeros = [1, 2, 3, 4, 5]
    print(f"{numeros} => {kata02_duplicar_lista(numeros)}")

    print("\n=== Kata 03 - encontrar coincidentes ===")
    palabras = ["dataset", "date", "delta", "Datas"]
    objetivo = "data"
    print(f"'{objetivo}' en {palabras} => {kata03_encontrar_coincidentes(palabras, objetivo)}")

    print("\n=== Kata 04 - diferencia entre listas ===")
    lista1 = [7, 22, 10, 42]
    lista2 = [6, 44, -4, 42]
    print(f"{lista1} - {lista2} => {kata04_diferencia_listas(lista1, lista2)}")

    print("\n=== Kata 05 - media con estado ===")
    notas = [7, 6, 10, 3]
    print(f"{notas} => {kata05_media_con_estado(notas)}")

    print("\n=== Kata 06 - factorial recursivo ===")
    try:
        num = 5
        print(f"{num} => {kata06_factorial_recursivo(num)}")
    except ValueError as e:
        print(f"{num} => Error valor negativo: {e}")
    except Exception as e:
        print(f"{num} => Error: {e}")

    print("\n=== Kata 07 - tuplas a string ===")
    lista_tuplas = [("Kata", 7), ("ThePower", "Python")]
    print(f"{lista_tuplas} => {kata07_tuplas_a_strings(lista_tuplas)}")

    print("\n=== Kata 08 - división segura ===")
    # kata08_division_segura()

    print("\n=== Kata 09 - filtrar mascotas ===")
    nombres_mascotas = ["Perro", "Tigre", "Gato", "Oso"]
    print(f"{nombres_mascotas} => {kata09_filtrar_mascotas(nombres_mascotas)}")

    print("\n=== Kata 10 - media segura ===")
    try:
        numeros = [7, 6, 10, 3]
        print(f"{numeros} => {kata10_media_segura(numeros)}")
    except ListaVaciaError as e:
        print(f"{numeros} => Error de datos: {e}")
    except Exception as e:
        print(f"{numeros} => Error: {e}")

    print("\n=== Kata 11 - pedir edad ===")
    # kata11_pedir_edad()

    print("\n=== Kata 12 - longitudes de palabras ===")
    frase = "Lorem ipsum dolor sit amet"
    print(f"'{frase}' => {kata12_longitudes_palabras(frase)}")

    print("\n=== Kata 13 - mayúscula y minúscula ===")
    caracteres = "PaTAta"
    print(f"'{caracteres}' => {kata13_mayuscula_minuscula(caracteres)}")

    print("\n=== Kata 14 - palabras que empiezan por ===")
    palabras = ["Dado", "Lápiz", "", "libro"]
    letra = "l"
    print(f"{palabras} empieza por '{letra}' => {kata14_palabras_que_empiezan_por(palabras, letra)}")

    print("\n=== Kata 15 - sumar tres con lambda ===")
    numeros = [1, 2, 3, 4, 5]
    print(f"{numeros} => {kata15_sumar_tres_lambda(numeros)}")

    print("\n=== Kata 16 - palabras mas largas que ===")
    frase = "Prepara los dados, la ficha y el bolígrafo"
    n = 6
    print(f"'{frase}' > {n} => {kata16_palabras_mas_largas_que(frase, n)}")

    print("\n=== Kata 17 - dígitos a número ===")
    digitos = [3, 1, 4]
    print(f"{digitos} => {kata17_digitos_a_numero(digitos)}")

    print("\n=== Kata 18 - filtrar mejores estudiantes ===")
    print(f"{kata18_filtrar_mejores_estudiantes()}")

    print("\n=== Kata 19 - filtrar impares con lambda ===")
    numeros = [1, 2, 3, 4, 5]
    print(f"{numeros} => {kata19_filtrar_impares_lambda(numeros)}")

    print("\n=== Kata 20 - filtrar enteros ===")
    valores = [False, "1", "dos", 3]
    print(f"{valores} => {kata20_filtrar_enteros(valores)}")

    print("\n=== Kata 21 - cubo con lambda ===")
    num = 5
    print(f"{num} => {kata21_cubo_lambda(num)}")

    print("\n=== Kata 22 - prodücto de una lista ===")
    numeros = [2, 5, 11, 2]
    print(f"{numeros} => {kata22_producto_lista(numeros)}")

    print("\n=== Kata 23 - concatenar palabras ===")
    palabras = ["beautiful", "is", "better", "than", "ugly"]
    print(f"{palabras} => {kata23_concatenar_palabras(palabras)}")

    print("\n=== Kata 24 - diferencia total ===")
    numeros = [42, 7, 9, 2]
    print(f"{numeros} => {kata24_diferencia_total(numeros)}")

    print("\n=== Kata 25 - contar caracteres ===")
    texto = "Python != Is Not is not"
    print(f"'{texto}' => {kata25_contar_caracteres(texto)}")

    print("\n=== Kata 26 - modulo con lambda ===")
    dividendo = 15
    divisor = 4
    print(f"{dividendo} % {divisor} => {kata26_modulo_lambda(dividendo, divisor)}")

    print("\n=== Kata 27 - promedio ===")

    print("\n=== Kata 28 - primer duplicado ===")

    print("\n=== Kata 29 - enmascarar ===")

    print("\n=== Kata 30 - son anagramas ===")

    print("\n=== Kata 31 - buscar nombre ===")

    print("\n=== Kata 32 - buscar puesto empleado ===")

    print("\n=== Kata 33 - sumar listas con lambda ===")

    print("\n=== Kata 34 - clase Arbol ===")

    print("\n=== Kata 35 - clase UsuarioBanco ===")

    print("\n=== Kata 36 - procesar texto ===")

    print("\n=== Kata 37 - momento del día ===")

    print("\n=== Kata 38 - nota a texto ===")

    print("\n=== Kata 39 - area ===")

    print("\n=== Kata 40 - descuento tienda online ===")
    