from normalization.components import *
from normalization.algorithms import *

if __name__ == "__main__":
    fd1 = FunctionalDependency("{A} -> {B, C}") #No es un subconjunto de A
    fd2 = FunctionalDependency("{A, B} -> {B}")

    print("Prueba de:")
    print("  ", fd1.is_trivial()) #false
    print("  ", fd2.is_trivial()) #True

if __name__ == "__main__": #CLOSURE 
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")

    df1 = FunctionalDependency("{A} -> {B}")
    df2 = FunctionalDependency("{B} -> {C}")

    conjunto = {A}
    dependencias = {df1, df2}

    resultado = closure(conjunto, dependencias)

    nombres = set()
    for atributo in resultado:
        nombres.add(atributo.name)

    print("\nPrueba del metodo closure:")
    print("  ","Cierre de {A}: ", nombres)  # Debería imprimir: {'A', 'B', 'C'}

    #COMPROBAMOS que si estemos bien
    esperado = {"A", "B", "C"}
    obtenido = nombres
    print(obtenido == esperado)  # Esto te imprime True si el cierre fue correcto

if __name__ == "__main__": #superllave
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")

    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{B} -> {C}")

    encabezado = {A, B, C}
    claves_posibles = {A}

    print("\n3- ¿Es superclave?", is_superkey(claves_posibles, encabezado, {fd1, fd2}))
    #Resultado correcto: A determina todo el encabezado -> es una superllave

if __name__ == "__main__": #llave
    # Creamos los atributos
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")

    # Creamos las dependencias funcionales
    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{B} -> {C}")

    # Definimos el encabezado
    encabezado = {A, B, C}

    # Prueba 1: A debería ser clave
    print("¿{A} es clave?", is_key({A}, encabezado, {fd1, fd2}))  # Esperamos True

    # Prueba 2: A, B no es clave porque no es irreducible
    print("¿{A, B} es clave?", is_key({A, B}, encabezado, {fd1, fd2}))  # Esperamos False

if __name__ == "__main__": #EJ1, FNBC
    fd1 = FunctionalDependency("{RFC} -> {Nombre, CP}")
    fd2 = FunctionalDependency("{FolioF} -> {RFC}")
    fd3 = FunctionalDependency("{FolioF} -> {MontoF, IVA, FechaF}")
    fd4 = FunctionalDependency("{FolioF} -> {RegimenF, CFDI}")
    fd5 = FunctionalDependency("{FolioP} -> {MontoP, FechaP}")
    fd6 = FunctionalDependency("{FolioP} -> {FolioF}")
    fd7 = FunctionalDependency("{MontoF} -> {IVA}")

    mvd1 = MultivaluedDependency("{RFC} ->-> {RegimenC}")

    relvar = Relvar(
        heading=["Nombre", "RFC", "CP", "RegimenF", "RegimenC", "CFDI", "FolioF", "MontoF", "IVA", "FechaF", "Producto", "FolioP", "MontoP", "FechaP"],
        functional_dependencies=[fd1, fd2, fd3, fd4, fd5, fd6],
        multivalued_dependencies=[mvd1]
    )

    print(f"Relvar: {relvar}")

    print("\nFunctional dependencies:")
    for fd in relvar.functional_dependencies:
        print(fd)

    print("\nMultivalued dependencies:")
    for mvd in relvar.multivalued_dependencies:
        print(mvd)

    print("¿La relación está en BCNF?", is_relvar_in_bcnf(relvar))

if __name__ == "__main__": #EJ2, FNBC
    # Atributos
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")

    # Dependencias funcionales
    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{A} -> {C}")

    # Creamos la relación
    relvar_bcnf = Relvar(
        heading=["A", "B", "C"],
        functional_dependencies=[fd1, fd2]
    )

    # Probamos si está en BCNF
    print("¿Relación simple está en BCNF?", is_relvar_in_bcnf(relvar_bcnf))

if __name__ == "__main__": #relvar en 4FN
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")

    mvd = MultivaluedDependency("{A} ->-> {B}")
    fd = FunctionalDependency("{A, C} -> {B}")

    relvar = Relvar(
        heading=["A", "B", "C"],
        functional_dependencies=[fd],
        multivalued_dependencies=[mvd]
    )

    print("¿Relación está en 4NF?", is_relvar_in_4nf(relvar))  # Esperamos False