import random
import time
import copy
# array base para todos los algoritmos
base_array = [random.randint(0, 999) for _ in range(5000)]

# Esta función se encarga de seleccionar cual algoritmo de ordenamiento se va a ejecutar

def launch_algorithm(algorithm):

    if algorithm == 'quicksort':

        start = time.time()
        quickSort(quicksort_array, 0, len(quicksort_array)-1)
        end = time.time()
        print(quicksort_array)
        print('')
        print('tiempo de ejecución',end-start, 'segundos')


    if algorithm == 'radixsort':

        start = time.time()
        radixSort(radixsort_array)
        end = time.time()
        print(radixsort_array)
        print('')
        print('timepo de ejecución: ',end-start, 'segundos')


    if algorithm == 'bubblesort':

        start = time.time()
        bubbleSort(bubblesort_array)
        end = time.time()
        print(bubblesort_array)
        print('')
        print('timepo de ejecución: ',end-start, 'segundos')


    if algorithm == 'mergesort':

        start = time.time()
        mergeSort(mergesort_array)
        end = time.time()
        print(mergesort_array)
        print('')
        print('timepo de ejecución: ',end-start, 'segundos')


    if algorithm == 'insertionsort':

        start = time.time()
        InsertionSort(insertionsort_array)
        end = time.time()
        print(insertionsort_array)
        print('')
        print('timepo de ejecución: ',end-start, 'segundos')


    if algorithm == 'selectionsort':

        start = time.time()
        largo = len(selectionsort_array)
        SelectionSort(selectionsort_array,largo)
        end = time.time()
        print(selectionsort_array)
        print('')
        print('timepo de ejecución: ',end-start, 'segundos')

# sección de QuickSort #########################################################
################################################################################
# Antonio Rojas

quicksort_array = copy.copy(base_array)

# Esta funcion se encarga de determinar si la cantidad de elementos en un determinado array es mayor a 1
# Llama a partition la cual está encargada de realizar el acomodo.
# También guarda como variable el return value de partition, el cuál es el pivot. Este se utiliza para acomodar los sub-arrays

def quickSort(array, left, right):
    if left < right: # Caso base (mientras tenga más de un elemento)
        partition_pos = partition(array, left, right)
        quickSort(array, left, partition_pos - 1)
        quickSort(array, partition_pos + 1, right)

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j: # Se mantiene hasta que i y j se cruzen o sean equivalentes
        while i < right and array[i] < pivot:
            i += 1

        while j > left and array[j] >= pivot:
            j -= 1

        if i < j: # Cambio de i y j
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot: # Una vez que ya no se cumpla la condición del while principal se realzia el cambio entre i y el pivot
        array[i], array[right] = array[right], array[i]

    return i

################################################################################
################################################################################

# sección de RadixSort #########################################################
################################################################################
# Diego Ortiz

radixsort_array = copy.copy(base_array)

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

########################################################################################
########################################################################################

# sección de BubbleSort ################################################################
#######################################################################################
# Adrian Monge

bubblesort_array = copy.copy(base_array)

#Se define una función llamada bubbleSort que recibe una lista
#llamada array como entrada. Esta función ordenará los elementos
#en la array en orden ascendente.
def bubbleSort(array):

# Recorrer cada elemento de la matriz
#Inicia un bucle for que itera sobre cada elemento de la array.
#La variable de bucle i variará de 0 a len(array) - 1.
  for i in range(len(array)):

    #Inicializa una variable llamada swapped a False.
    #Esta palabra reservada se utilizará para registrar si
    #se han producido intercambios durante la pasada actual del bucle interno.
    swapped = False

    #Inicia un bucle for anidado (bucle interno) que itera sobre la array para comparar elementos adyacentes.
    #La variable de bucle j variará de 0 a len(array) - i - 1.
    #Este rango optimizado asegura que los elementos ya ordenados en pasadas anteriores no se vuelvan a comparar.
    for j in range(0, len(array) - i - 1):

      #Compara dos elementos adyacentes en los índices j y j + 1.
      #Si el elemento en el índice j es mayor que el elemento en el índice j + 1,
      #significa que no están en el orden deseado.
      if array[j] > array[j + 1]:

        #Crea una variable temporal temp para almacenar el valor del elemento en el índice j.
        #Esto es necesario para evitar sobrescribir el valor original durante el intercambio.
        temp = array[j]
        #Coloca el valor del elemento en el índice j + 1 (el elemento más grande) en el elemento en el índice j.
        array[j] = array[j+1]
        #Coloca el valor previamente almacenado del elemento en el índice j (el elemento más pequeño) en el elemento en el índice j + 1. Esto completa el intercambio.
        array[j+1] = temp
        #Establece la bandera swapped en True para indicar que se produjo un intercambio durante la pasada actual.
        swapped = True

    #Comprueba si la bandera swapped es False. Si es False,
    #significa que no se han producido intercambios en la pasada actual del bucle interno,
    #lo que indica que la matriz ya está ordenada.
    if not swapped:
      break

########################################################################################
########################################################################################

# sección de MergeSort ################################################################
#######################################################################################
# Adrian Monge

mergesort_array = copy.copy(base_array)

def mergeSort(array):
  """Ordena una lista de elementos en orden ascendente usando el algoritmo Merge Sort.

  Args:
      array (list): La lista a ordenar.

  Returns:
      list: La lista ordenada.
  """

  # Caso base: Si la lista tiene un solo elemento o está vacía, ya está ordenada
  if len(array) > 1:

    # Encontrar el punto medio de la lista
    r = len(array) // 2

    # Dividir la lista en dos sublistas: izquierda (L) y derecha (M)
    L = array[:r]  # Rebanada desde el inicio hasta el punto medio (exclusivo)
    M = array[r:]  # Rebanada desde el punto medio hasta el final

    # Ordena recursivamente las sublistas izquierda y derecha
    mergeSort(L)
    mergeSort(M)

    # Índices para recorrer las sublistas L y M, y el índice para la lista principal (array)
    i = j = k = 0

    # Fusionar las sublistas ordenadas L y M en la lista principal array
    while i < len(L) and j < len(M):
      # Comparar el primer elemento sin fusionar de cada sublista
      if L[i] < M[j]:
        # Si el elemento de L es menor, lo agregamos a array y avanzamos en L
        array[k] = L[i]
        i += 1
      else:
        # Si el elemento de M es menor, lo agregamos a array y avanzamos en M
        array[k] = M[j]
        j += 1
      # En ambos casos, avanzamos en el índice de la lista principal (array)
      k += 1

    # Copiar los elementos restantes de la sublista L (si existen)
    while i < len(L):
      array[k] = L[i]
      i += 1
      k += 1

    # Copiar los elementos restantes de la sublista M (si existen)
    while j < len(M):
      array[k] = M[j]
      j += 1
      k += 1

########################################################################################
########################################################################################

# sección de InsertionSort #############################################################
#######################################################################################
# Jimena Campos

insertionsort_array = copy.copy(base_array)

def InsertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Comparar la clave con cada elemento a su izquierda hasta encontrar un elemento menor que ella.
        # Para orden descendente, cambiar clave<matriz[j] por clave>matriz[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Coloca la llave a continuación del elemento justo más pequeño que ella.
        array[j + 1] = key

########################################################################################
########################################################################################

# sección de SelectionSort #############################################################
#######################################################################################
# Jimena Campos

selectionsort_array = copy.copy(base_array)

def SelectionSort(array, largo):

    for step in range(largo):
        min_idx = step

        for i in range(step + 1, largo):

            # para ordenar en orden descendente, cambiar > por < en esta línea
            # seleccionar el elemento mínimo en cada bucle
            if array[i] < array[min_idx]:
                min_idx = i

        # poner min en la posición correcta
        (array[step], array[min_idx]) = (array[min_idx], array[step])

########################################################################################
########################################################################################

# Se llama a la funcion de ejecución
# Los llamados son: quicksort, insertionsort, bubblesort, mergesort, radixsort y selectionsort

launch_algorithm('quicksort')