from Spiel import Spiel as Game

class Turnier:
    """
    Die Turnierklasse enthaelt alle Spiele und kann eine Auswertung ueber diese
    zusammenstellen.
    """    
    def __init__(self, S1, S2, Spielfeld):
        """
        Constructor
        S1 soll Spieler1, den beginnenden Spieler beinhalten.
        S2 soll Spieler2 beinhalten.
        Spielfeld erwartet eine Collection aus Ganzzahlen.
        """
        self._Spieler = [S1, S2]
        self._Spielfeld = Spielfeld
        self._Spiele = []

    def _laeuftSpiel(self):
        """
        Es werden alle Spiele abgefragt, ob sie noch aktiv sind.
        """
        # wenn ein Spiel in der Liste noch aktiv ist, wird True zurueckgegeben
        for Spiel in self._Spiele:
            if Spiel.isAlive():

                # ein aktives Spiel gefunden
                return True

        # kein Spiel mehr aktiv, False zurueckgeben
        return False
        
    def start(self, count):
        """
        Die Spiele werden initialisiert und gestartet.
        Die Anzahl gestarteter Spiele wird im
        Parameter count festgelegt.
        """
        # Spielthreads initialisieren
        for i in range(count):

            # es werden die Spieler und eine Kopie des Spielfeldes
            # an Spiel uebergeben.
            s = Game(self._Spieler, self._Spielfeld.copy())
            self._Spiele.append(s)

        # Spielthreads starten
        for Spiel in self._Spiele:
            Spiel.start()
            
        # warten bis Threads beendet sind
        while self._laeuftSpiel():
            pass

    def result(self):
        """
        Als Ergebnis des Turnieres wird eine Stringliste mit
        den Resultaten der Spiele zusammengebaut.
        """
        # initialisieren der Rueckgabe.

        # Es Logg soll den Log von einem gewonnenen Spiel enthalten,
        Logg = ["nicht vorhanden"]
        
        # Logv soll den Log eines verlorenen Spiel enthalten.
        Logv = ["nicht vorhanden"]
        
        gewonnen = 0
        verloren = 0
        
        for Spiel in self._Spiele:
            
            # falls das Spiel von Spieler1 gewonnen wurde:
            if Spiel.winner == 0:
                gewonnen = gewonnen + 1
                Logg = Spiel.Log.LogSpiel
                
            # falls das Spiel von Spieler2 gewonnen wurde:
            else:
                verloren = verloren + 1
                Logv = Spiel.Log.LogSpiel

        # die Stringliste fuer die Rueckgabe wird zusammengebaut.
        result = [
            "Gewonnene Spiele Spieler1: " + str(100 * gewonnen / (gewonnen + verloren)) + "%",
            "Verlorene Spiele Spieler1: " + str(100 * verloren / (gewonnen + verloren)) + "%",
            "Beispiel eines von Spieler1 gewonnenen Spiels:",
            ]
        
        # der Log von einem gewonnenen Spiel wird hinzugefuegt.
        result = result + Logg
        
        result.append("Beispiel eines von Spieler1 verlorenen Spiels:")
        
        # der Log von einem verlorenen Spiel wird hinzugefuegt.
        result = result + Logv
        return result
