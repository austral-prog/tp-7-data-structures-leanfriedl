# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)

    Returns:
        Un string con la coordenada del mapa
    """
    coordenada = registro[1]
    return coordenada


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """
    letra = coordenada[0]
    numero = coordenada[1]
    return (letra, numero)


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.

    - Registro de Azara: (tesoro, coordenada) -> ej: ('Brass Spyglass', '4B')
    - Registro de Rui: (ubicacion, coordenada, cuadrante) ->
      ej: ('Abandoned Lighthouse', ('4', 'B'), 'Blue')

    Si las coordenadas coinciden, retornar una tupla combinada:
    (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    Si NO coinciden, retornar el string "not a match".

    Args:
        registro_azara: Tupla (tesoro, coordenada)
        registro_rui: Tupla (ubicacion, coordenada, cuadrante)

    Returns:
        Tupla combinada si las coordenadas coinciden, o "not a match" si no.
    """
    tesoro = registro_azara[0]
    coordenada_azara = registro_azara[1]
    ubicacion = registro_rui[0]
    coordenada_rui = registro_rui[1]
    cuadrante = registro_rui[2]
    numero_rui = coordenada_rui[0]
    letra_rui = coordenada_rui[1]
    coordenada_rui_pegada = numero_rui + letra_rui

    if coordenada_azara == coordenada_rui_pegada:
        return (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)
    else:
        return "not a match"


def sum_tuple(numeros):
    """
    Recorre una tupla de números y retorna la suma total.
    Si la tupla está vacía, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo la tupla con un for (o while).

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos de la tupla

    Ejemplo:
        sum_tuple((1, 2, 3, 4, 5)) -> 15
        sum_tuple(()) -> 0
    """
    total = 0
    if len(numeros) == 0:
        return total
    for numero in numeros:
        total += numero
    return total


def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.

    No se permite usar el método .count(). Implementar el conteo
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos de cualquier tipo
        elemento: El elemento a contar

    Returns:
        La cantidad de veces que aparece el elemento (int)

    Ejemplo:
        count_occurrences((1, 2, 2, 3, 2), 2) -> 3
        count_occurrences(('a', 'b', 'a'), 'c') -> 0
    """
    total = 0
    if len(tupla) > 0:
        elemento1 = tupla[0]
        if elemento1 == elemento:
            total += 1
    if len(tupla) > 1:
        elemento2 = tupla[1]
        if elemento2 == elemento:
            total += 1
    if len(tupla) > 2:
        elemento3 = tupla[2]
        if elemento3 == elemento:
            total += 1
    if len(tupla) > 3:
        elemento4 = tupla[3]
        if elemento4 == elemento:
            total += 1
    if len(tupla) > 4:
        elemento5 = tupla[4]
        if elemento5 == elemento:
            total += 1
    if len(tupla) > 5:
        elemento6 = tupla[5]
        if elemento6 == elemento:
            total += 1
    if len(tupla) > 6:
        elemento7 = tupla[6]
        if elemento7 == elemento:
            total += 1
    return total


def find_index(tupla, elemento):
    """
    Recorre la tupla y retorna el índice de la PRIMERA aparición del
    elemento. Si el elemento no se encuentra, retorna -1.

    No se permite usar el método .index(). Implementar la búsqueda
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos
        elemento: El elemento a buscar

    Returns:
        El índice (int) de la primera aparición, o -1 si no está

    Ejemplo:
        find_index(('a', 'b', 'c', 'b'), 'b') -> 1
        find_index((1, 2, 3), 9) -> -1
    """
    numero_elem = len(tupla)
    if numero_elem > 0:
        if tupla[0] == elemento:
            return 0
    if numero_elem > 1:
        if tupla[1] == elemento:
            return 1
    if numero_elem > 2:
        if tupla[2] == elemento:
            return 2
    if numero_elem > 3:
        if tupla[3] == elemento:
            return 3
    if numero_elem > 4:
        if tupla[4] == elemento:
            return 4
    if numero_elem > 5:
        if tupla[5] == elemento:
            return 5
    if numero_elem > 6:
        if tupla[6] == elemento:
            return 6
    if numero_elem > 7:
        if tupla[7] == elemento:
            return 7
    return -1

def filter_positives(numeros):
    """
    Recorre una tupla de números y retorna una nueva tupla con solo
    los números positivos (> 0). El cero NO se considera positivo.

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        Tupla con los números positivos, en el orden original

    Ejemplo:
        filter_positives((-3, 1, 0, 5, -2, 7)) -> (1, 5, 7)
        filter_positives((-1, -2, -3)) -> ()
    """
    lista_positivos = []
    for numero in numeros:
        if numero > 0:
            lista_positivos.append(numero)
    return tuple(lista_positivos)

