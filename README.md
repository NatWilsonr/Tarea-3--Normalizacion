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

Las siguientes pruebas están implementadas en el archivo `pruebasMain.py`.  
Cada una está separada y comentada claramente para identificar qué función se está evaluando.  

Puede ejecutar todo con:
```bash
python pruebasMain.py
```


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

