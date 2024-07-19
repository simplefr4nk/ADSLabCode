from DS.MinHeap import MinHeap
from DS.MaxHeap import MaxHeap

"""
#---------- QUICK SELECT ----------#
"""

def partition(arr, p, q) -> int:
    x = arr[q]
    i = p - 1
    for j in range(p, q):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[q] = arr[q], arr[i + 1]
    return i+1

def quick_select_rec(arr, k, p, q) -> int:
    """Funzione ricorsiva sull'intervallo [p, q] di arr che termina restituendo il k-esimo elemento più piccolo
    
    Parameters
    ----------
    arr : List[int]
        Vettori di interi
    k : int
        Indice del k-esimo elemento
    p : int
        Limite inferiore di analisi. p >= 0
    q : int
        Limite superiore di analisi. p < q < len(arr)
    
    Returns
    -------
    int
        k-esimo valore più piccolo

    """
    
    r = partition(arr, p, q)
    if k == r or not (p <= k <= q):
        return arr[k]
    elif k < r:
        return quick_select_rec(arr, k, p, r-1)
    else:
        return quick_select_rec(arr, k, r+1, q)

def QuickSelect(arr, k) -> int:
    """Implementazione algoritmo quick select
    
    Parameters
    ----------
    arr : List[int]
        Vettore di interi
    k : int
        Posizione

    Returns
    -------
    int
        Valore k-esimo elemento più piccolo.
        None se len(arr) < k

    """

    if not (0 <= k-1 <= len(arr)-1):
        return None
    return quick_select_rec(arr, k-1, 0, len(arr)-1)


"""
#---------- MEDIAN OF MEDIANS ----------#
"""

def Select(A, index):
    """Funzione che trova il valore che si troverebbe alla posizione index se il
    vettore fosse ordinato, senza ordinare il vettore

    Parameters
    ----------
    A     : List[int]
          Vettore di valori interi
    index : int
          Indice del k-esimo elemento

    Returns
    -------
    int
        K-esimo valore più piccolo

    """
    # usa 1 per indicare il primo elemento
    if index > 0:
        index -=1
    else: # se trova 0 ritorna None
        return None

    return selectRec(A, 0, len(A)-1, index)

def selectRec(A, start, end, index):
    """Funzione ricorsiva e inPlace che trova il valore che si troverebbe alla
    posizione index se il vettore fosse ordinato, senza ordinare il vettore

    Parameters
    ----------
    A     : List[int]
          Vettore di valori interi
    start : int
          Indice del inizio del sottovettore
    end   : int
          Indice della fine del sottovettore
    index : int
          Indice del k-esimo elemento

    Returns
    -------
    int
        K-esimo valore più piccolo

    """

    # fino a che A non è divisibile in blocchi da 5 elementi
    while (end - start + 1) % 5 != 0:
        # per ogni elemento nel subArray
        for j in range(start + 1, end + 1):
            # se è il più piccolo
            if A[start] > A[j]:
                # swap di A[start] con A[j] --> sposta il minimo al primo 
                # elemento del subArray
                A[start], A[j] = A[j], A[start]
        # se ci serve il numero alla posizione iniziale di un subArray che non 
        # è multiplo di 5 lo ritorna subito
        if index == 0:
            return A[start]
        # messo il minimo in A[start] incremento start e diminuisco l'indice
        # index perché la dimensione del vettore preso in considerazione diminuisce
        start += 1
        index -= 1

    numberSubArray = (end - start + 1) // 5

    for j in range(numberSubArray):
        insertionSort(A, start + j * 5, start + j * 5 + 4)
        A[start + j * 5], A[start + j * 5 + 2] = A[start + j * 5 + 2], A[start + j * 5]

    medianOfMedians = selectRec(A, start, start + numberSubArray - 1, (numberSubArray - 1) // 2)

    pivotIndex = partitionAround(A, start, end, medianOfMedians)

    pivotPosition = pivotIndex - start

    if index == pivotPosition:
        return A[pivotIndex]
    elif index < pivotPosition:
        return selectRec(A, start, pivotIndex - 1, index)
    else:
        return selectRec(A, pivotIndex + 1, end, index - pivotPosition - 1)

def partitionAround(A, start, end, pivot):
    """Modifica del Partition usato nel Quicksort per ruotare intorno al perno

    Parameters
    ----------
    A     : List[int]
          Vettore di interi
    start : int
          Indice del inizio del sottovettore
    end   : int
          Indice della fine del sottovettore
    pivot : int
          Mediano dei mediani su cui viene effettuata la rotazione
    
    Returns
    -------
    int
        Indice del pivot situato nel sottovettore

    """

    for i in range(start, end + 1):
        if A[i] == pivot:
            A[i], A[end] = A[end], A[i]
            break

    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1

def insertionSort(A, start, end):
    """Implementazione di insertion sort in Place per il Select

    Parameters
    ----------
    A     : List[int]
          Vettore di interi
    start : int
          Indice da dove parte il vettore da riordinare in A
    end   : int
          Indice dove finisce il vettore da riordinare in A

    """

    for i in range(start + 1, end + 1):
        key = A[i]
        j = i - 1
        while j >= start and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

"""
#---------- HEAP SELECT ----------#
"""

def HeapSelect(arr, k) -> int:
    if not 1 <= k <= len(arr):
        return None

    # Scelta ottimizzata della struttura dati.
    # Il k-esimo elemento minimo è lo (n-k)-esimo valore massimo
    if k < len(arr)/2:
        h1 = MinHeap()
        h2 = MinHeap()
    else:
        k = len(arr)-k+1
        h1 = MaxHeap()
        h2 = MaxHeap()

    h1.build(arr)
    h2.insert(h1.root)
    for _ in range(1, k):
        t = h2.extract()
        tl = h1.left(t.pos)
        tr = h1.right(t.pos)
        if tl:  # t ha un figlio sinistro?
            h2.insert(tl)
        if tr:  # t ha un figlio destro?
            h2.insert(tr)

    return h2.extract().val
