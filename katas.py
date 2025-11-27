from functools import reduce

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
    pass


def kata07_tuplas_a_strings(lista_tuplas):
    """
    Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
    """
    pass


def kata08_division_segura():
    """
    Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
    """
    pass


def kata09_filtrar_mascotas(nombres_mascotas):
    """
    Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
    """
    pass


def kata10_media_segura(numeros):
    """
    Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
    """
    pass


def kata11_pedir_edad():
    """
    Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
    """
    pass


def kata12_longitudes_palabras(frase):
    """
    Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
    """
    pass


def kata13_casos_caracteres(caracteres):
    """
    Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
    """
    pass


def kata14_palabras_que_empiezan_por(palabras, letra):
    """
    Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
    """
    pass


def kata15_sumar_tres_lambda(numeros):
    """
    Crea una función lambda que sume 3 a cada número de una lista dada.
    """
    pass


def kata16_palabras_mas_largas_que(palabras, n):
    """
    Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
    """
    pass


def kata17_digitos_a_numero(digitos):
    """
    Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
    """
    pass


def kata18_filtrar_mejores_estudiantes():
    """
    Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
    """
    pass


def kata19_filtrar_impares_lambda(numeros):
    """
    Crea una función lambda que filtre los números impares de una lista dada.
    """
    pass


def kata20_filtrar_enteros(valores):
    """
    Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
    """
    pass


def kata21_cubo_lambda(num):
    """
    Crea una función que calcule el cubo de un número dado mediante una función lambda.
    """
    pass


def kata22_producto_lista(numeros):
    """
    Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
    """
    pass


def kata23_concatenar_palabras(palabras):
    """
    Concatena una lista de palabras. Usa la función reduce().
    """
    pass


def kata24_diferencia_total(numeros):
    """
    Calcula la diferencia total en los valores de una lista. Usa la función reduce().
    """
    pass


def kata25_contar_caracteres(texto):
    """
    Crea una función que cuente el número de caracteres en una cadena de texto dada.
    """
    pass


def kata26_modulo_lambda(dividendo, divisor):
    """
    Crea una función lambda que calcule el resto de la división entre dos números dados.
    """
    pass


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
