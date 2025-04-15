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

