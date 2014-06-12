# -*- coding: utf-8 -*-
class OutputBuilder:
    """
    kümmert sich um das Schreiben in die Ausgabedatei
    """
    def __init__(self, Filename):
        """
        Constructor
        Filename erwartet den Pfad zur Ausgabedatei als str
        """
        self._Filename = Filename

    def write(self, lines):
        """
        schreibt den Inhalt der Stringliste lines in die Ausgabedatei
        """
        f = open(self._Filename, "w")
        # das Schreiben erfolgt Zeilenweise
        for line in lines:
            pline = str(line) + "\n"
            f.write(pline)
        
