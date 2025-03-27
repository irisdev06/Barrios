# *NumPy*

---

## *Paso 1: Instalación y primeros pasos*
NumPy usa álgebra lineal optimizada para cálculos eficientes.

python
pip install numpy
import numpy as np
np.array([1, 2, 3, 4, 5])


---

## *Paso 2: Crear arreglos de diferentes dimensiones*

### *1D: Vector*
python
np.array([1, 2, 3])

\[
\mathbf{v} = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}
\]

### *2D: Matriz*
python
np.array([[1, 2, 3], [4, 5, 6]])

\[
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}
\]

### *Matrices especiales*
python
np.zeros((3,3))
np.ones((2,2))

\[
Z = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\]
\[
O = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\]

---

## *Paso 3: Propiedades básicas*
python
arr.shape  # Dimensiones
arr.ndim   # Número de dimensiones
arr.dtype  # Tipo de dato


---

## *Paso 4: Operaciones básicas*

### *1. Operaciones elemento a elemento*
python
A + B
A * B

\[
A + B = \begin{bmatrix} 5 & 7 & 9 \end{bmatrix}
\]

### *2. Operaciones con escalares*
python
A * 2

\[
A \times 2 = \begin{bmatrix} 2 & 4 & 6 \end{bmatrix}
\]

### *3. Funciones matemáticas*
python
np.sqrt(A)

\[
\sqrt{A} = \begin{bmatrix} 2 & 3 & 4 \end{bmatrix}
\]

---

## *Paso 5: Indexación y segmentación*
python
arr[1:3]  # Segmentación
arr[arr > 2]  # Indexación booleana


---

## *Paso 6: Cambiar la forma de los arreglos*
python
A.reshape(2,3)  # Redimensionar
A.flatten()  # Aplanar


---

## *Paso 7: Operaciones avanzadas*

### *1. Producto punto*
python
np.dot(A, B)

\[
A \cdot B = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
\]

### *2. Transpuesta*
python
A.T

\[
A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
\]

### *3. Estadísticas*
python
np.mean(A)

\[
\mu = \frac{1+2+3}{3} = 2
\]

---

## *Paso 8: Generación de números aleatorios*
python
np.random.rand(3,3)  # Matriz aleatoria
np.random.randint(0,10,(2,2))  # Matriz de enteros aleatorios


---