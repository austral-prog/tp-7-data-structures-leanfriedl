# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    inventario = {}
    for elemento in items:
        cantidad = items.count(elemento)
        inventario[elemento] = cantidad
    return inventario


def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    for elemento in items:
        if elemento in inventario:
            inventario[elemento] += 1
        else:
            inventario[elemento] = 1
    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    for elemento in items:
        if elemento in inventario:
            # Restar solo si hay stock
            if inventario[elemento] > 0:
                inventario[elemento] -= 1
        else:
            # Si el item no existe en inventario, se ignora o se inicializa en 0
            inventario[elemento] = 0
            if inventario[elemento] == 0:
                del inventario[elemento]
    return inventario

def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    if item in inventario:
        del inventario[item]
    return inventario


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    lista_de_tuplas = []
    for elemento, cantidad in inventario.items():
        if cantidad > 0:
            tupla_individual = []
            tupla_individual.append(elemento)
            tupla_individual.append(cantidad)
            lista_de_tuplas.append(tuple(tupla_individual))

    return lista_de_tuplas


def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".
    """
    if not diccionario:
        return ""
    return max(diccionario, key=diccionario.get)


def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido
    """
    diccionario_invertido = {}
    lista_valores = []
    for clave in diccionario:
        valor = diccionario[clave]
        lista_valores.append(valor)
        apariciones_de_valor = lista_valores.count(valor)
        if apariciones_de_valor > 1:
            diccionario_invertido[valor] += clave
        else:
            diccionario_invertido[valor] = clave

    return diccionario_invertido


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                      un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    diccionario_frecuencia_palabras = {}
    for palabra in palabras:
        apariciones = palabras.count(palabra)
        if apariciones == 0:
            return {}
        else:
            diccionario_frecuencia_palabras[palabra] = apariciones

    return diccionario_frecuencia_palabras


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    categoria_mayor = ""
    mayor_promedio = 0
    if len(gastos) > 0:
        for categoria, lista_gastos in gastos.items():
            suma = sum(lista_gastos)
            cantidad = len(categoria)
            promedio = suma / cantidad

            if promedio > mayor_promedio:
                mayor_promedio = promedio
                categoria_mayor = categoria

    return categoria_mayor


def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    totales = {}
    for categoria, lista in gastos.items():
        totales[categoria] = sum(lista)
    return totales


def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    totales = {}
    for categoria, lista in gastos.items():
        for tipo, monto in lista:
            totales[tipo] = totales.get(tipo, 0) + monto
    return totales
