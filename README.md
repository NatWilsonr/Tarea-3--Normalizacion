# ITAM Primavera 2025 - Tarea de Normalización

🏫 Integrantes del equipo: 
- Nayade Velasco Acosta
- Eduardo Medina Valdes
- Victor Manuel Benitez Renteria
- Ana Paola Carmona Mendez 
- Karol Josafat Cisneros Juarez
- Natalia Wilson Robles

---

## 📘 Descripción

Este proyecto implementa funciones relacionadas con la teoría de normalización de bases de datos.


---

## 🤝 Nat-nota para el equipo (temporal)

### 📂 Sobre `components.py`

Este archivo contiene las **clases principales** del modelo relacional:

- `Attribute`: representa un atributo (como A, B, C...)
- `Dependency`: clase base para dependencias funcionales y multivaluadas
- `FunctionalDependency`: representa dependencias como `{A} -> {B}`
- `MultivaluedDependency`: representa dependencias como `{A} ->-> {B}`
- `Relvar`: representa una relación (una tabla), que incluye:
  - Encabezado (atributos)
  - Conjunto de dependencias funcionales
  - Conjunto de dependencias multivaluadas

🔧 **TODOs resueltos aquí:**
- `FunctionalDependency.is_trivial()`
- `MultivaluedDependency.is_trivial(heading)`

---

### ⚙️ Sobre `algorithms.py`

Este archivo contiene las funciones que hacen el "trabajo pesado" de normalización:

- `closure(...)`: calcula el cierre de un conjunto de atributos
- `is_superkey(...)`: revisa si un conjunto de atributos determina todo el encabezado (es superllave)
- `is_key(...)`: revisa si un conjunto es llave (irreducible)
- `is_relvar_in_bcnf(...)`: determina si una relación está en BCNF
- `is_relvar_in_4nf(...)`: determina si una relación está en 4NF

🔧 **TODOs resueltos aquí:**
- `closure`
- `is_superkey`
- `is_key`
- `is_relvar_in_bcnf`
- `is_relvar_in_4nf`

---

### Pruebas agregadas (en `pruebasMain.py`)

Se implementaron pruebas para verificar que cada función funciona correctamente, incluyendo:

- `is_trivial()` para DFs
- `closure()` con dependencias en cadena
- `is_superkey()` y `is_key()` con conjuntos válidos y no válidos
- `is_relvar_in_bcnf()` con ejemplos que cumplen y no cumplen
- `is_relvar_in_4nf()` con ejemplos que cumplen y no cumplen

➡️ Ver `pruebasMain.py` para ver cada sección delimitada, con comentarios claros y separadores visuales.

---

🧼 *Esta sección es temporal y puede borrarse antes de entrega final si el README ya está claro para todos.*



---


## 💻 Configuración

Este proyecto no tiene dependencias adicionales de Python, por lo que no es 
necesario crear un ambiente virtual. Está desarollado y probado con Python 3.13,
pero debe funcionar con 3.8 o superior.



## 🗂️ Estructura
- `components.py`: Estructuras base y validaciones de dependencias
- `algorithms.py`: Lógica de normalización paso a paso
- `exceptions.py`: Validaciones para errores de expresión o encabezado inválido
- `pruebasMain.py`: Pruebas automáticas con comentarios organizados
- `example.py`: Ejemplo realista preconstruido (incluido en la tarea)




## 💡 Suposiciones
- Se considera que el encabezado (heading) de una relación incluye todos los atributos posibles.
- Las dependencias se ingresan con el formato "{A, B} -> {C}" y "{X} ->-> {Y}".
- Todas las verificaciones de llave y superllave se basan en cierres funcionales.
- Las clases Attribute, FunctionalDependency y MultivaluedDependency son utilizadas como estructuras base

## 🧪 Ejemplos de uso con resultados esperados

| Prueba | Descripción | Resultado esperado |
|--------|-------------|--------------------|
| 1 | Verifica si una DF es trivial | True o False |
| 2 | Calcula el cierre de {A} con A→B y B→C | {'A', 'B', 'C'} |
| 3 | Verifica si {A} es superclave en {A, B, C} | True |
| 4 | Verifica si {A} es clave mínima y {A, B} no lo es | True, False |
| 5 | Relación compleja con dependencias reales | No está en BCNF |
| 6 | Relación pequeña con A→B, A→C | Está en BCNF |
| 7 | Relación con MVD no trivial y determinante no superclave | No está en 4NF |
| 8 | Relación con MVD trivial y determinante superclave | Está en 4NF |

