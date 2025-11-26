# PROYECTO 3 - Katas Python

# Este tercer proyecto consiste en completar, validar y entregar todos los ejercicios de Python que se plantean a continuación:

def kata01_char_frequency(text):
    """
    Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
    """
    frequencies = {}
    for c in text:
        if c != " ":
            frequencies[c] = frequencies.get(c, 0) + 1
    return frequencies

def kata02_duplicate_list(numbers):
    """
    Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
    """
    return list(map(lambda num: num*2, numbers))

def kata03_find_matching_words(words, target):
    """
    Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
    """
    target_clean = target.strip().lower()
    if not target_clean:
        return []
    
    return list(filter(lambda w: target_clean in w.lower(), words))

def kata04_diff_lists(list1, list2):
    """
    Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
    """
    pass

def kata05_average_with_status(numbers, nota_aprobado=5):
    """
    Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
    """
    pass

def kata06_factorial(n):
    """
    Escribe una función que calcule el factorial de un número de manera recursiva.
    """
    pass

def kata07_tuples_to_strings(tuples_list):
    """
    Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
    """
    pass

def kata08_safe_division():
    """
    Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
    """
    pass

def kata09_filter_pets(pet_names):
    """
    Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
    """
    pass

def kata10_safe_average(numbers):
    """
    Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
    """
    pass

def kata11_ask_age():
    """
    Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
    """
    pass

def kata12_word_lengths(sentence):
    """
    Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
    """
    pass

def kata13_char_cases(chars):
    """
    Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
    """
    pass

def kata14_words_starting_with(words, letter):
    """
    Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
    """
    pass

def kata15_add_three_lambda(numbers):
    """
    Crea una función lambda que sume 3 a cada número de una lista dada.
    """
    pass

def kata16_words_longer_than(words, n):
    """
    Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
    """
    pass

def kata17_digits_to_number(digits):
    """
    Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
    """
    pass

def kata18_filter_top_students():
    """
    Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
    """
    pass

def kata19_filter_odds_lambda(numbers):
    """
    Crea una función lambda que filtre los números impares de una lista dada.
    """
    pass

def kata20_filter_integers(values):
    """
    Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
    """
    pass

def kata21_cube_lambda(n):
    """
    Crea una función que calcule el cubo de un número dado mediante una función lambda.
    """
    pass

def kata22_list_product(numbers):
    """
    Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
    """
    pass

def kata23_concatenate_words(words):
    """
    Concatena una lista de palabras. Usa la función reduce().
    """
    pass

def kata24_total_difference(numbers):
    """
    Calcula la diferencia total en los valores de una lista. Usa la función reduce().
    """
    pass

def kata25_count_chars(text):
    """
    Crea una función que cuente el número de caracteres en una cadena de texto dada.
    """
    pass

def kata26_mod_lambda(a, b):
    """
    Crea una función lambda que calcule el resto de la división entre dos números dados.
    """
    pass

def kata27_average(numbers):
    """
    Crea una función que calcule el promedio de una lista de números.
    """
    pass

def kata28_first_duplicate(items):
    """
    Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
    """
    pass

def kata29_mask_string(value):
    """
    Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
    """
    pass

def kata30_are_anagrams(word1, word2):
    """
    Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
    """
    pass

def kata31_find_name_in_input():
    """
    Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
    """
    pass

def kata32_find_employee_position(full_name, employees):
    """
    Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
    """
    pass

def kata33_sum_lists_lambda(list1, list2):
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

    def quitar_rama(self, position):
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

    def __init__(self, name, balance, has_checking_account):
        pass

    def retirar_dinero(self, amount):
        pass

    def transferir_dinero(self, other_user, amount):
        pass

    def agregar_dinero(self, amount):
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

def kata37_time_of_day():
    """
    Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
    """
    pass

def kata38_grade_to_text(score):
    """
    Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
     · Reglas:
       0 - 69:  insuficiente
      70 - 79:  bien
      80 - 89:  muy bien
      90 - 100: excelente
    """
    pass

def kata39_area(figure, data):
    """
    Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
    """
    pass

def kata40_online_store_discount():
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

    print("\n=== Kata 01 ===")
    text = "Contar palabras"
    print(f"{text} => {kata01_char_frequency(text)}")

    print("\n=== Kata 02 ===")
    numbers = [1, 2, 3, 4, 5]
    print(f"{numbers} => {kata02_duplicate_list(numbers)}")

    print("\n=== Kata 03 ===")
    words = ["dataset", "date", "delta", "Datas"]
    target = "data"
    print(f"{target}, {words} => {kata03_find_matching_words(words, target)}")
