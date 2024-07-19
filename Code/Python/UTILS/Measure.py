import time

# Costante del errore minimo nella misurazione
E = 0.001

def resolution():
    """Funzione che trova la risoluzione minima delle misurazioni di tempo
    utilizzando il clock monotonico

    Returns
    -------
    float
         Risoluzione minima
    
    """

    # inizia a contare
    start = time.perf_counter()
    # attende una esecuzione di una funzione singola
    while time.perf_counter() == start:
        pass
    # finisce di contare
    stop = time.perf_counter()
    # ritorna il tempo passato tra l'inizio e la fine
    return stop - start

def minMeasureTime():
    """Funzione che trova la minor tempo misurabile delle misurazioni di tempo
    utilizzando il clock monotonico

    Returns
    -------
    float
         Risoluzione minima
    
    """
    return resolution() * (1/E +1)

def Measure(A, K, Tmin, Algo):
    """Funzione che misura il tempo di esecuzione della funzione select

    Parameters
    ----------
    A      : List[int]
           Vettore di interi
    length : int
           Lunghezza del vettore
    K      : int
           Indice del k-esimo elemento
    Tmin   : int
           Risoluzione del metodo di misura
    Algo   : func()
           Algoritmo da misurare

    Returns
    -------
    float
         Risoluzione minima
    
    """

    count = 0
    start_time = time.perf_counter()
    while True:
        Algo(A, K)
        count = count + 1
        end_time = time.perf_counter()
        if end_time - start_time >= Tmin:
            break
    return (end_time - start_time) / count