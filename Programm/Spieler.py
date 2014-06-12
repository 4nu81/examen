"""
Diese Datei enthaelt die Klassen der Spieler1 und Spieler2.
Die Basisklasse Spieler ist ebenfalls enthalten. Die Spieler
realisieren das Verhalten unter bestimmten Bedingungen auf dem
Spielfeld.
"""

import random

class Spieler:
    """
    Basisklasse fuer alle Spieler mit grundlegender Funktionalitaet
    """
    def __init__(self, name):
        """
        Constructor
        """
        self.name = name        

    # soll von den Erben ueberschrieben werden. Beinhaltet die Spieler-
    # Strategie
    def _tactic(self, Feld, count, row, val):
        """
        Leere Methode, die von den Spielerklassen ueberschrieben werden soll
        """
        raise UsrError("Methode der Basisklasse muss ueberschrieben werden.")

    def Zug(self, Feld):
        """
        wird vom Spiel aufgerufen, wenn der Spieler einen Spielzug
        ausfuehren soll. Alle Spieler die diese Methode nicht ueberschreiben,
        gewinnen, falls nur noch Hoelzer in einer Reihe existieren. Sonst wird
        die individuelle Strategie, die in _tactic implementiert ist, angewendet.
        """
        row = -1
        val = -1
        count = 0
        # Zaehlen der Reihen mit Hoelzern.
        for i in range(len(Feld)):

            # Wenn nicht leere Reihe gefunden
            if Feld[i] > 0:

                # Anzahl an Reihen mit Hoelzern erhoehen.
                count = count + 1
                
                # merkt sich die letzte Reihe mit Inhalt.
                # so kann sofort auf diese zurueckgegriffen werden,
                # falls es nur eine Reihe gibt.
                row = i

        # ist die Anzahl der Reihen Groesser 1
        if count > 1:
            # wird die implementierte Taktic verwendet.
            res = self._tactic(Feld, count, row, val)
            row = res[0]
            val = res[1]
        else:
            # sonst soll verbliebene Reihe elemeniert werden.
            val = Feld[row]

        # Rueckgabe der Reihe und der Anzahl von Hoelzern die
        # weggenommen werden sollen.
        return [row, val]

class Spieler2(Spieler):
    """
    Spieler2s Verhalten wurde in der Aufgabenstellung eindeutig beschrieben.
    Er soll eine beliebige Menge an Hoelzern aus einer beliebigen Reihe
    entnehmen.
    """
    def _tactic(self, Feld, count, row, val):
        """
        Legt Spieler2s Verhalten fest, falls mehr als eine Reihe Hoelzer enthalten
        """
        # Zuerst eine Reihe zufaellig waehlen
        # randint(a,b) gibt einen zufaelligen Wert aus dem Intervall
        # [a,b] zurueck. (inclusive a und b)
        j = random.randint(1, count)

        # Index der Reihe finden.
        for i in range(len(Feld)):
            if Feld[i] > 0:
                j = j - 1
                if j == 0:
                    row = i
                    break
        # einen beliebigen Wert zwischen aus dem Interval [1,Feldvalue] finden
        # randint(a,b) gibt einen zufaelligen Wert aus dem Intervall
        # [a,b] zurueck. (inclusive a und b)
        val = random.randint(1, Feld[row])

        # Spalte und Value zurueckgeben
        return [row, val]

class Spieler1(Spieler):
    """
    Spieler eins implementiert die in der Dokumentation beschriebene, vom
    Pruefling entwickelte Taktik
    """
    def _tactic(self, Feld, count, row, val):

        # ist die Anzahl nicht leerer Reihen groesser 2
        if count > 2:
            
            #soll die Reihe mit dem kleinsten Wert gefunden werden.
            val = 9
            for i in range(len(Feld)):
                if Feld[i] < val and Feld[i] != 0:
                    row = i
                    val = Feld[i]
        # sonst
        else:
            r1 = -1
            r2 = -1
            
            # finden der beiden Reihen
            for i in range(len(Feld)):
                if Feld[i] > 0:
                    if r1 == -1:
                        r1 = i
                    else:
                        r2 = i
                        
            # falls beide den gleichen Wert haben, soll er ein Holz aus der
            # ersten Reihe entnehmen
            if Feld[r1] == Feld[r2]:
                val = 1
                row = r1

            # falls beide einen unterschiedlichen Wert haben,
            # soll er die Reihen ausgleichen
            else:
                if Feld[r1] < Feld[r2]:
                    val = Feld[r2] - Feld[r1]
                    row = r2
                else:
                    val = Feld[r1] - Feld[r2]
                    row = r1
        # Reihe und Wert zurueckgeben
        return [row, val]
