# -*- coding: utf-8 -*-
class Log:
    """
    logt die einzelnen Simulationsschritte in LogSpiel
    """
    def __init__(self):        
        """
        Constructor
        """
        self.LogSpiel = []

    def LogZug(self, spieler, before, after):
        """
        logt sich einen Spielzug. Die Anzahl der Spielzüge ist gleich der
        Anzahl an Logeinträgen. Daher reichen die Informationen
        Spieler, before und after aus. Aus denen wird eine Logzeile
        zusammengesetzt und gespeichert.
        """
        msg = "Zug%s , %s : %s -> %s" % (str( len(self.LogSpiel) + 1 ),
                                         spieler.name,
                                         str(before),
                                         str(after),
                                         )
        # Collections in Strings umgewandelt, enthalten eckige Klammern.
        # In der Beispielausgabe wurden runde Klammern verwendet,
        # weshalb ich diese hier ersetze.
        msg = msg.replace("[", "(").replace("]", ")")
        self.LogSpiel.append(msg)
