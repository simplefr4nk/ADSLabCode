class IndexedValue:
    """Valore con annessa posizione (astratta)

    Attributes
    ----------
    val : int
        Valore
    pos : int
        Posizione elemento
    
    """
    
    def __init__(self, val, pos=None):
        self.val = val
        self.pos = pos
