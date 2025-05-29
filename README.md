# 🔄 Algoritmos de Ordenamiento en Python

## 📋 Descripción

Este repositorio implementa y compara los principales algoritmos de ordenamiento utilizando Python. Se evalúa el rendimiento de seis algoritmos diferentes ordenando una lista de 5000 números enteros generados aleatoriamente.

## 📊 Algoritmos Implementados

- **QuickSort**: Algoritmo de división y conquista que selecciona un elemento como pivote y particiona el array
- **RadixSort**: Algoritmo no comparativo que ordena enteros procesando dígitos individuales
- **BubbleSort**: Algoritmo simple que compara repetidamente pares adyacentes de elementos
- **MergeSort**: Algoritmo de división y conquista que divide, ordena y combina subconjuntos
- **InsertionSort**: Construye una secuencia ordenada un elemento a la vez
- **SelectionSort**: Selecciona repetidamente el elemento mínimo del array no ordenado

## 🧪 Funcionamiento del Código

El programa genera una lista aleatoria de 5000 números enteros (de 0 a 999) y luego:
1. Crea una copia de la lista para cada algoritmo
2. Mide el tiempo de ejecución de cada algoritmo
3. Muestra la lista ordenada y el tiempo empleado
4. Permite comparar el rendimiento entre los distintos métodos

## 🚀 Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/Preko700/algoritmos-ordenamiento.git

# Navegar al directorio
cd algoritmos-ordenamiento

# Ejecutar el script
python ordenamiento.py
```

Para probar un algoritmo específico, modifica la última línea del código:

```python
# Para probar el algoritmo QuickSort:
launch_algorithm('quicksort')

# Para probar otros algoritmos:
# launch_algorithm('radixsort')
# launch_algorithm('bubblesort')
# launch_algorithm('mergesort')
# launch_algorithm('insertionsort')
# launch_algorithm('selectionsort')
```

## 📈 Complejidad Algorítmica

| Algoritmo | Mejor caso | Caso promedio | Peor caso | Espacio |
|-----------|------------|---------------|-----------|---------|
| QuickSort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| RadixSort | O(nk) | O(nk) | O(nk) | O(n+k) |
| BubbleSort | O(n) | O(n²) | O(n²) | O(1) |
| MergeSort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| InsertionSort | O(n) | O(n²) | O(n²) | O(1) |
| SelectionSort | O(n²) | O(n²) | O(n²) | O(1) |

*Donde n es el número de elementos y k es el número de dígitos del valor máximo*

## 🔍 Detalles de Implementación

### QuickSort
QuickSort selecciona un elemento como "pivote" y reorganiza los elementos para que los menores que el pivote queden a su izquierda y los mayores a su derecha. Luego aplica el mismo proceso recursivamente a cada partición.

```python
def quickSort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)
        quickSort(array, left, partition_pos - 1)
        quickSort(array, partition_pos + 1, right)
```

### RadixSort
RadixSort ordena los números procesando dígito por dígito, desde el menos significativo hasta el más significativo. Utiliza CountingSort como subrutina.

```python
def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
```

### BubbleSort
BubbleSort compara repetidamente pares adyacentes de elementos, intercambiándolos si están en el orden incorrecto. El proceso se repite hasta que no se necesiten más intercambios.

```python
def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
```

### MergeSort
MergeSort divide la lista en mitades, ordena cada mitad recursivamente y luego fusiona las mitades ordenadas.

```python
def mergeSort(array):
    if len(array) > 1:
        r = len(array) // 2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        # Fusionar las sublistas ordenadas
        i = j = k = 0
        # ...código de fusión...
```

### InsertionSort
InsertionSort construye la lista ordenada un elemento a la vez, insertando cada nuevo elemento en su posición correcta.

```python
def InsertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
```

### SelectionSort
SelectionSort divide la lista en una parte ordenada y otra no ordenada. Repetidamente selecciona el elemento más pequeño de la parte no ordenada y lo coloca al final de la parte ordenada.

```python
def SelectionSort(array, largo):
    for step in range(largo):
        min_idx = step
        for i in range(step + 1, largo):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
```

## 📊 Resultados Esperados

Basado en la complejidad de los algoritmos, para una lista de 5000 elementos se esperaría:

1. **QuickSort** y **MergeSort**: Los más rápidos (ms o pocos segundos)
2. **RadixSort**: Rápido si los números no tienen muchos dígitos (comparable con QuickSort)
3. **InsertionSort**: Velocidad moderada-baja (segundos)
4. **SelectionSort** y **BubbleSort**: Los más lentos (varios segundos)

El tiempo exacto dependerá del hardware y del orden inicial de los elementos.

## 🛠️ Mejoras Posibles

- Implementar paralelismo para los algoritmos que lo permiten (MergeSort, QuickSort)
- Añadir visualizaciones del proceso de ordenamiento
- Implementar variaciones de los algoritmos (QuickSort con diferentes estrategias de pivote)
- Añadir funcionalidad para generar gráficos comparativos de rendimiento

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## 👨‍💻 Autores

- Antonio Rojas (QuickSort)
- Diego Ortiz (RadixSort)
- Adrian Monge (BubbleSort, MergeSort)
- Jimena Campos (InsertionSort, SelectionSort)

Desarrollado como parte del curso de Introducción a la Programación del Tecnológico de Costa Rica, como parte del plan de estudios de la Ingeniería en Computadores.
