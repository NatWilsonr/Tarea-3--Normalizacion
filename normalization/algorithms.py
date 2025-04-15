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


def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 4
    raise NotImplementedError()


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 5
    raise NotImplementedError()


def is_relvar_in_bcnf(relvar: Relvar):
    # TODO: Actividad 6
    raise NotImplementedError()


def is_relvar_in_4nf(relvar: Relvar):
    # TODO: Actividad 7
    raise NotImplementedError()
