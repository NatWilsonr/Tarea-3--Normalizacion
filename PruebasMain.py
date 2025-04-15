from normalization.components import *
from normalization.algorithms import *

if __name__ == "__main__":
    print("=" * 40)
    print("1. Pruebas de is_trivial para dependencias funcionales")
    fd1 = FunctionalDependency("{A} -> {B, C}")  # No trivial
    fd2 = FunctionalDependency("{A, B} -> {B}")  # Trivial
    print("  Resultado 1:", fd1.is_trivial())  # False
    print("  Resultado 2:", fd2.is_trivial())  # True

    print("\n" + "=" * 40)
    print("2. Prueba del método closure")
    A = Attribute("A")
    B = Attribute("B")
    C = Attribute("C")
    df1 = FunctionalDependency("{A} -> {B}")
    df2 = FunctionalDependency("{B} -> {C}")
    conjunto = {A}
    dependencias = {df1, df2}
    resultado = closure(conjunto, dependencias)
    nombres = {attr.name for attr in resultado}
    print("  Cierre de {A}:", nombres)
    print("  Resultado esperado:", nombres == {"A", "B", "C"})

    print("\n" + "=" * 40)
    print("3. Prueba de is_superkey")
    encabezado = {A, B, C}
    print("  ¿{A} es superllave?", is_superkey({A}, encabezado, {df1, df2}))

    print("\n" + "=" * 40)
    print("4. Prueba de is_key")
    print("  ¿{A} es llave?", is_key({A}, encabezado, {df1, df2}))      # True
    print("  ¿{A, B} es llave?", is_key({A, B}, encabezado, {df1, df2}))  # False

    print("\n" + "=" * 40)
    print("5. Ejemplo de Relvar original (no cumple BCNF)")
    fd1 = FunctionalDependency("{RFC} -> {Nombre, CP}")
    fd2 = FunctionalDependency("{FolioF} -> {RFC}")
    fd3 = FunctionalDependency("{FolioF} -> {MontoF, IVA, FechaF}")
    fd4 = FunctionalDependency("{FolioF} -> {RegimenF, CFDI}")
    fd5 = FunctionalDependency("{FolioP} -> {MontoP, FechaP}")
    fd6 = FunctionalDependency("{FolioP} -> {FolioF}")
    mvd1 = MultivaluedDependency("{RFC} ->-> {RegimenC}")
    relvar = Relvar(
        heading=["Nombre", "RFC", "CP", "RegimenF", "RegimenC", "CFDI",
                 "FolioF", "MontoF", "IVA", "FechaF", "Producto", "FolioP", "MontoP", "FechaP"],
        functional_dependencies=[fd1, fd2, fd3, fd4, fd5, fd6],
        multivalued_dependencies=[mvd1]
    )
    print("  ¿Relvar está en BCNF?", is_relvar_in_bcnf(relvar))

    print("\n" + "=" * 40)
    print("6. Ejemplo que SÍ cumple BCNF")
    fd1 = FunctionalDependency("{A} -> {B}")
    fd2 = FunctionalDependency("{A} -> {C}")
    relvar_bcnf = Relvar(
        heading=["A", "B", "C"],
        functional_dependencies=[fd1, fd2]
    )
    print("  ¿Relvar está en BCNF?", is_relvar_in_bcnf(relvar_bcnf))  # True

    print("\n" + "=" * 40)
    print("7. Ejemplo que NO cumple 4NF")
    mvd = MultivaluedDependency("{A} ->-> {B}")
    fd = FunctionalDependency("{A, C} -> {B}")
    relvar_4nf_fail = Relvar(
        heading=["A", "B", "C"],
        functional_dependencies=[fd],
        multivalued_dependencies=[mvd]
    )
    print("  ¿Relvar está en 4NF?", is_relvar_in_4nf(relvar_4nf_fail))  # False

    print("\n" + "=" * 40)
    print("8. Ejemplo que SÍ cumple 4NF")
    # Aquí A es superllave
    mvd2 = MultivaluedDependency("{A} ->-> {B}")
    relvar_4nf_pass = Relvar(
        heading=["A", "B", "C"],
        functional_dependencies=[FunctionalDependency("{A} -> {C}")],
        multivalued_dependencies=[mvd2]
    )
    print("  ¿Relvar está en 4NF?", is_relvar_in_4nf(relvar_4nf_pass))  # True
