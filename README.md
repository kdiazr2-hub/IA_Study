# IA_Study

Ruta personal para aprender **Python, matemáticas, machine learning e IA**, paso a paso,
con apuntes, ejercicios y proyectos pequeños.

## Cómo trabajamos

1. Cada módulo tiene su carpeta con un `README.md`: objetivos, lecturas y ejercicios.
2. Los ejercicios son scripts (`.py`) o notebooks (`.ipynb`). Se resuelven, se ejecutan y se revisan.
3. Al terminar un tema se marca con `[x]` en el registro de avances de abajo.
4. Las dudas y los apuntes propios van en un archivo `notas.md` dentro de cada módulo.

## Ruta de estudio

| # | Módulo | Carpeta | Libro principal |
|---|--------|---------|-----------------|
| 1 | Python sólido | [`01_python/`](01_python/) | Learning Python (Lutz) |
| 2 | Datos con NumPy y pandas | [`02_datos/`](02_datos/) | Python for Data Analysis (McKinney) |
| 3 | Matemáticas para ML | [`03_matematicas/`](03_matematicas/) | Linear Algebra Notes, Practical Statistics |
| 4 | Machine learning | [`04_ml/`](04_ml/) | Data Science from Scratch, Hands-On ML caps. 1–9 |
| 5 | Deep learning | [`05_deep_learning/`](05_deep_learning/) | Hands-On ML caps. 10–19 |
| 6 | IA clásica | [`06_ia/`](06_ia/) | Artificial Intelligence (Poole y Mackworth) |

Los módulos 2 y 3 pueden avanzar en paralelo: las matemáticas se practican con NumPy.

## Registro de avances

### 1. Python
- [ ] Diagnóstico inicial (`01_python/00_diagnostico.py`)
- [ ] Tipos, cadenas, listas, diccionarios, tuplas y conjuntos
- [ ] Control de flujo, comprensiones e iteradores
- [ ] Funciones: argumentos, alcance, lambdas y closures
- [ ] Módulos, paquetes y entornos virtuales
- [ ] Clases y programación orientada a objetos
- [ ] Excepciones y archivos
- [ ] Generadores y decoradores
- [ ] Proyecto: mini-aplicación de consola

### 2. Datos
- [ ] NumPy: arrays, vectorización y broadcasting
- [ ] pandas: Series, DataFrame, selección y filtrado
- [ ] Limpieza y transformación de datos
- [ ] Agrupación y agregación (`groupby`)
- [ ] Visualización con matplotlib
- [ ] Proyecto: análisis exploratorio de un dataset real

### 3. Matemáticas
- [ ] Álgebra lineal: vectores, matrices y producto matricial
- [ ] Álgebra lineal: rango, inversa, autovalores y autovectores
- [ ] Cálculo: derivadas, regla de la cadena y gradientes
- [ ] Probabilidad: distribuciones y teorema de Bayes
- [ ] Estadística: muestreo, intervalos y pruebas de hipótesis
- [ ] Descenso de gradiente programado desde cero

### 4. Machine learning
- [ ] Regresión lineal y logística desde cero
- [ ] Proyecto ML completo (Hands-On cap. 2)
- [ ] Clasificación y métricas
- [ ] SVM, árboles y ensembles
- [ ] Reducción de dimensionalidad y clustering
- [ ] Proyecto: modelo de principio a fin

### 5. Deep learning
- [ ] Redes neuronales y retropropagación desde cero
- [ ] Keras: redes densas
- [ ] Redes convolucionales (CNN)
- [ ] Redes recurrentes y secuencias
- [ ] Transformers y atención
- [ ] Proyecto de deep learning

### 6. IA clásica
- [ ] Agentes y búsqueda (BFS, DFS, A*)
- [ ] Satisfacción de restricciones
- [ ] Razonamiento con incertidumbre
- [ ] Planificación y aprendizaje por refuerzo

## Biblioteca (`libros/`)

- **Learning Python**, 4.ª ed. Mezcla Python 2 y 3, así que algunas partes están anticuadas.
- **Python for Data Analysis**, 3.ª ed.
- **Linear Algebra Review and Reference** (Stanford CS229)
- **Practical Statistics for Data Scientists**
- **Data Science from Scratch**
- **Hands-on ML with Scikit-Learn, Keras & TensorFlow**, 2.ª ed., libro completo.
- *Hands-On ML with Scikit-Learn & TensorFlow* (`_compressed`, 279 págs.): versión preliminar,
  solo caps. 1–9. Está repetida y se puede borrar.
- **Artificial Intelligence, 3rd Ed. – Python Code**
- `otros/`: material fuera de esta ruta (Kali Linux).

## Entorno

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
