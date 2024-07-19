from DS.IndexedValue import IndexedValue

class MinHeap:
    """Implementazione personalizzata di Min-Heap.
    Ogni elemento è di tipo IndexedValue, dove l'attributo val contiene il valore
    (oggetto delle condizioni di correttezza della struttura dati) e l'attributo pos contenente la posizione all'interno dell'albero (array).
    
    Properties
    ----------
    root : IndexedValue
        Elemento radice della Min-Heap (eq. getmin())

    """

    def __init__(self):
        self.__v : list[IndexedValue] = [] # Lista di IndexedValue

    def __swap(self, i, j):
        self.__v[i], self.__v[j] = self.__v[j], self.__v[i]

    def __heapify(self, i):
        l = self.__left(i) + 1
        r = self.__right(i) + 1
        
        m = l if (l < self.length() and self.__v[l].val < self.__v[i].val) else i

        if r < self.length() and self.__v[r].val < self.__v[m].val:
            m = r

        if m != i:
            self.__swap(i, m)
            self.__heapify(m)

    def __parent(self, i) -> int:
        # Funzione interna per il calcolo della posizione 
        # del padre dell'elemento i  
        return int((i-1)/2)

    def __left(self, i) -> int:
        # Funzione interna per il calcolo della posizione 
        # del figlio sx dell'elemento i  
        return 2*i

    def __right(self, i) -> int:
        # Funzione interna per il calcolo della posizione 
        # del figlio dx dell'elemento i  
        return 2*i+1
    

    def left(self, i) -> IndexedValue:
        """Figlio sinistro
        
        Parameters
        ----------
        i : int
            Posizione dell'elemento di cui prendere il figlio sx

        Returns
        -------
        IndexedValue
            Figlio sinistro dell'elemento i

        """
        
        ic = self.__left(i)
        return self.__v[ic-1] if ic <= self.length() else None
    
    def right(self, i) -> IndexedValue:
        """Figlio destro
        
        Parameters
        ----------
        i : int
            Posizione dell'elemento di cui prendere il figlio dx

        Returns
        -------
        IndexedValue
            Figlio destro dell'elemento i

        """
        
        ic = self.__right(i)
        return self.__v[ic-1] if ic <= self.length() else None

    @property
    def root(self) -> IndexedValue:
        return self.__v[0] if len(self.__v) > 0 else None

    def build(self, xn):
        """Inizializzazione tramite array

        Parameters
        ----------
        xn : List[int]
            Lista di elementi da inserire

        """

        self.__v = [IndexedValue(el) for el in xn]
        for i in range(int(len(xn)/2), -1, -1):
            self.__heapify(i)

        # Salvataggio indice per il ripescaggio dei figli
        for idx, el in enumerate(self.__v):
            el.pos = idx + 1

    def length(self) -> int:
        """Numero di elementi nella heap"""

        return len(self.__v)

    def getmin(self) -> IndexedValue:
        """Valore minimo heap"""

        return self.root

    def extract(self) -> IndexedValue:
        """Rimozione della radice
        
        Returns
        -------
        int
            Valore radice estratta

        """

        if self.length() < 1:
            raise IndexError("Min-Heap is empty")

        self.__swap(0, self.length()-1)
        el = self.__v.pop()
        self.__heapify(0)
        return el

    def insert_val(self, x: int):
        """Inserimento valore nella Min-Heap
        
        Parameters
        ----------
        x : int
            Valore da inserire

        """

        self.insert(IndexedValue(x))

    def insert(self, x: IndexedValue):
        """Inserimento elemento nella Min-Heap
        
        Parameters
        ----------
        x : IndexedValue
            IndexedValue da inserire

        """

        if not x.pos:
            x.pos = self.length() + 1

        self.__v.append(x)
        i = self.length()-1
        while self.__v[i].val <= self.__v[self.__parent(i)].val and i > 0:
            p = self.__parent(i)
            self.__swap(i, p)
            i = p
