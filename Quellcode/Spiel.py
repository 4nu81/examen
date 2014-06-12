# -*- coding: utf-8 -*-
from threading import Thread
from Log import Log

"""
Das Spiel bildet eine Spielrunde des Nim-Spiels ab.
Die Spieler werden abwechselnd nach ihrem naechsten Zug gefragt und
dieser wird dann dokumentiert.
"""
class Spiel(Thread):
    
    def __init__(self, Spieler, Spielfeld):
        """
        Constructor
        Spieler erwartet eine Collection mit den beiden Spielern
        Spielfeld erwartet eine Collection von Ganzzahlen
        """
        self._Spieler = Spieler
        self._Spielfeld = Spielfeld
        Thread.__init__(self)
        self.winner = -1
        self.Log = Log()

    def _checkZug(self, row, val):
        """
        Hier wird die Gueltigkeit des vom Spieler gewaehlten Zug geprueft.
        Gueltig ist er nur, wenn in der gewaehlten Reihe
        noch genuegend Hoelzer existieren.
        """
        # optimistische behandlung. Erst wenn eine Bedingung nicht
        # erfuellt ist, wird result auf False gesetzt.
        result = True

        # Es koennen nur Fehler Auftreten, wenn auf einen nicht
        # vorhandenen Index zugegriffen werden soll. Daher ist
        # diese Pruefung in einen Try-Except Block gefasst.
        try:
            t = self._Spielfeld[row]

            # val muss zwischen 1 und der Anzahl der Hoelzer liegen.
            if val > t or val < 1:
                result = False
        except:
            result = False
        return result

    def _checkWin(self):
        """
        Hier wird die Siegbedingung geprueft. Sie ist gegeben, wenn
        alle Hoelzer aufgenommen wurden.
        """
        # optimistische Behandlung. Erst wenn die Bedingung nicht
        # erfuellt ist, wird result auf False gesetzt.
        result = True
        for val in self._Spielfeld:
            if val != 0:
                result = False
        return result

    def run(self):
        """
        Run beschreibt den Ablauf des Spieles.
        """
        IndexTemp = 0
        Index = 0

        # solange nicht gewonnen wurde
        while not self._checkWin():

            # Soll der Spieler der an der Reihe ist einen Zugvorschlag machen
            a = self._Spieler[Index].Zug(self._Spielfeld)

            # Wenn dieser Zugvorschlag gueltig ist
            if self._checkZug(a[0], a[1]):

                # wird sich der Spielerindex gemerkt
                IndexTemp = Index

                # wird das Spielfeld kopiert (um den Log das Feld vor und
                # nach der Aenderung zu uebergeben.
                after = self._Spielfeld.copy()

                # Der Zug durchgefuehrt
                after[a[0]] = after[a[0]] - a[1]

                # und in den Log geschrieben
                self.Log.LogZug(self._Spieler[Index], self._Spielfeld, after)

                # dem Spielfeld das Geaenderte Spielfeld uebergeben
                self._Spielfeld = after

                # der Naechste Spieler ermittelt.
                Index = (Index+1) % len(self._Spieler)

        # wenn gewonnen wurde, wird sich der Spielerindex des Gewinners gemerkt
        self.winner = IndexTemp        
