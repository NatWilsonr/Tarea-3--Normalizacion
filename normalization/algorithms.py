from .components import FunctionalDependency, Attribute, Relvar


    #La funcion recibe:
        #attributes: un conjunto inicial (por ejemplo {A})
        #functional_dependencies: un conjunto de objetos (como { A → B, B → C })
def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    # TODO: Actividad 3
    #Dado un conjunto de atributos X, y un conjunto de dependencias funcionales E, el cierre de
    # X, (X+), es el conjunto de todos los atributos que puedes deducir a partir de X usando las reglas de E.

    #Creamos una copia del conjunto original (X⁺)
    cierre = set(attributes)

    #Bandera para saber si se agregaron atributos nuevos 
    se_agrego_algo = True

    #Mientras sigamos encontrando nuevas dependencias funcionales aplicables, agregamos más atributos
    while se_agrego_algo:
        se_agrego_algo = False  # Suponemos que esta vez no se agregará nada
    
    # Recorremos cada dependencia funcional, primero A → B, luego B → C.
        for df in functional_dependencies:
            lado_izquierdo = df.determinant
            lado_derecho = df.dependant

            #¿Todos los atributos del lado izquierdo están ya en el cierre actual?
            es_aplicable = True
            for atributo in lado_izquierdo:
                if atributo not in cierre:
                    es_aplicable = False
                    break

            # Entonces agregamos los del lado derecho (si no estaban ya)
            if es_aplicable: #Si la dependencia es aplicable 
                for atributo in lado_derecho:
                    if atributo not in cierre:
                        cierre.add(atributo)
                        se_agrego_algo = True  # Como sí agregamos, volvemos a repetir el ciclo While

      #Paso final: regresamos el cierre
    return cierre    

    #La funcion recibe: 
        #attributes → el conjunto X
        #Heading → el conjunto E (encabezado)
        #functional_dependencies → el conjunto de dependencias funcionales F
def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 4
    #Un conjunto de atributos X es un superkey si su cierre determina el encabezado E
    
    #Obetenemos el cierre de los conjuntos dados
    cierre = closure(attributes, functional_dependencies)

    #bandera de resultado
    es_superclave = True  # Si no faltó ninguno, sí es superclave

    #Verificamos si el cierre contiene todos los atributos del encabezado
    for atributo in heading:
        if atributo not in cierre:
            es_superclave = False  # Si falta uno, no es superclave

    return es_superclave


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 5
    #un conjunto de atributos es X es una llave si:
        #1- X es una superllave (Todas las llaves son Super llaves, pero NO todas las Superllaves son llaves)
        #2- Que sea irreducible (No puedes quitarle ningún atributo sin que deje de ser superclave)

    #Verificamos si X es una superllave -> en caso de que NO, entonces ya no hacemos lo demás 
    if not is_superkey(attributes, heading, functional_dependencies):
        return False
    
    #Lo convertimos a lista para poder quitar uno por uno
    lista_atributos = list(attributes)

    #Revisamos todos los subconjuntos que resultan al quitar un atributo
    for atributo in range( len(lista_atributos) ):
        subconjunto = set()  # Creamos un subconjunto vacío

    # Agregamos todos menos el i-ésimo
        for j in range( len(lista_atributos) ):
            if atributo != j:
                subconjunto.add( lista_atributos[j] )

        # Revisamos si ese subconjunto también es superclave
        if is_superkey( subconjunto, heading, functional_dependencies ):
            return False  # No es irreducible

    # Si no hubo subconjunto que fuera superclave, entonces sí es clave
    return True


def is_relvar_in_bcnf(relvar: Relvar):
    # TODO: Actividad 6
    #Una relación está en FNBC si todas sus dependencias funcionales no triviales cumplen que:
    # El determinante (lado izquierdo) sea superclave.

    #Obtenemos los atributos del encabezado
    encabezado = relvar.heading

    #Recorremos cada dependencia funcional
    for df in relvar.functional_dependencies:
        lado_izquierdo = df.determinant
        lado_derecho = df.dependant

        # Verificamos si es una dependencia NO trivial
        es_trivial = True
        for atributo in lado_derecho:
            if atributo not in lado_izquierdo:
                es_trivial = False
                break #nos salimos del ciclo

        # Si no es trivial...
        if not es_trivial:
            # ...el lado izquierdo debería ser superclave
            if not is_superkey(lado_izquierdo, encabezado, relvar.functional_dependencies):
                return False  # Si alguna no cumple, no está en BCNF

    # Si todas las dependencias no triviales cumplen, entonces sí está en BCNF
    return True


def is_relvar_in_4nf(relvar: Relvar):
    # TODO: Actividad 7
    raise NotImplementedError()
