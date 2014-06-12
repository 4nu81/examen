"""
Controler zum starten der Simulation des Nim-Spiels.
Benutzung:
Controler.py [InputFilename]

InputFilename muss vom Typ ".in" sein, sonst kann das Programm die Datei nicht
oeffnen. Ausgegeben wird das Ergebnis der Simulation in eine gleichnamige Datei
mit der Endung ".out"

Die Inputfile kann beliebig viele Kommentarzeilen vor den Startbedingungen
enthalten. Die Startbedingungen geben dann die Anzahl an Reihen und deren
Groesse an. Es darf 1 bis 9 Reihen geben mit einem Startwert zwischen 1 und 9.
Angegeben werden diese durch 1 bis 9 durch Leerzeichen voneinander getrennte
Ganzzahlen zwischen 1 und 9 in der ersten Zeile ohne Kommentar.

Alle folgenden Zeilen werden ignoriert.
"""

import sys, os
from Spieler import Spieler1, Spieler2
from Turnier import Turnier
from FeldBuilder import FeldBuilder
from OutputBuilder import OutputBuilder
from UsrError import UsrError, UsrNeedHelp
from LogConsole import LogConsole
     

def getArgs():
    """
    baut aus den Parametern die dem Programm uebergeben wurden eine neue
    String-Liste. Somit muss nicht mehr auf die globalen Parameter zugegriffen
    werden.
    """
    result = []
    try:
        for arg in sys.argv:
            s = arg
            result.append(s)
    except:
        print('Fehler beim Parameter lesen')
        raise Exception()
    else:
        return result

# Extrahiert den Dateinamen aus den Args und prueft diesen auf Richtigkeit
def getFilename():
    """
    Prueft ob es genau einen Parameter gab und ob dieser einen gueltigen
    Dateipfad enthaelt.

    Als Zusaetzliche nicht geforderte Funktion gibt der Parameter 'help'
    auf der Konsole einen Hilfetext aus.
    """
    result = ""
    args = getArgs()
    # args.append("test.in") #wurde zur Entwicklungszeit benoetigt
    if len(args) == 2: # es sollte genau ein Parameter uebergeben werden.
                    # args[0] zeigt dabei auf die ausgefuehrte datei selbst.
        result = args[1]
    else:
        if len(args) < 2:            
            raise UsrError("Keinen Dateinamen angegeben")
        if len(args) > 2:
            raise UsrError("Zu viele Argumente angegeben")
    if result.lower() == "help":
        raise UsrNeedHelp()
    if not result.endswith(".in"):
        raise UsrError("Datei falschen Typs uebergeben")
    if not os.path.exists(result):
        raise UsrError("Datei %s kann nicht gefunden werden" % (result,))
    return result
    

# Abweichung da es eine Statische Methode ist und somit
# keine Objektreferenz auf Turnier hat.
def baueAusgabe(Filename, Turnier):
    """
    Die Eingabedatei und die Turnierergebnisse werden hier
    fuer die Ausgabe zusammengefuehrt.
    """
    result = []
    last = Turnier.result() # Die Turnierergebnisse
    first = []    
    for line in open(Filename, "r"): # Der Eingabedatei-Inhalt        
        first.append(line)
    for line in first:
        line = line.replace("\n", " ")
    result = first + last
    return result

# Hauptprogramm
def main():
    """
    Dies ist der Controler fuer das Nim-Spiel.

    Der Controler bereitet alle notwendigen Daten
    fuer das Ausfuehren des Programms vor und interagiert mit dem OS um z.b. auf
    der Festplatte Daten zu lesen oder zu schreiben.

    Dann laesst er die Simulation ablaufen und schreibt die Ergebnisse in die
    Ausgabedatei
    """
    try:
        # Zur Dokumentation der Testfälle wird diese LogConsole verwendet.
        # Alle Ausgaben auf die Console und in die Ausgabedatei
        # sollen auch hier geloggt werden.
        Log = LogConsole()
        Log.msgList(sys.argv)
        
        # Initialisierung der Simulation
        f = getFilename() # liest den Filename aus den argv (Programmstart-Parameter)
        F = FeldBuilder() 
        Feld = F.getFeld(f) # versucht das Spielfeld zu bauen
        S1 = Spieler1("Spieler1")
        S2 = Spieler2("Spieler2")
        T = Turnier(S1,S2,Feld) # Initialisiert das Turnier
        
        T.start(10) # startet das Turnier (hier 10 Spiele) und wartet auf Ende
                    # aller Spiele (laufen als Threads)
                    
        O = OutputBuilder(f.replace(".in", ".out"))
                            # Initialisiert die Ausgabedatei.
                            # Falls diese bereits existiert, werden die Ergebnisse
                            # angehangen. Die Endung in Filename wird vorab noch in
                            # '.out' geaendert.
        lines = baueAusgabe(f,T)
        Log.msgList(lines)        
        O.write(lines) # Schreibt Spielergebnisse in die Ausgabedatei

    # dieser Bereich verarbeitet ausgeloeste Exceptions im Programm.
    except UsrError as e:
        Log.msg(e.msg)
        Log.msg("rufe 'Controler.py help' auf um mehr zu erfahren.")
        Log.msg(" ")
        Log.msg("==================================================")
        Log.msg(" ")
        print(e.msg)
        print("rufe 'Controler.py help' auf um mehr zu erfahren.")
        return 1
        # sys.exit(1) bedeutet, das die Excepion im Programm behandelt wurde,
        # also als Fehlerbehandlung programmiert wurde.
    except UsrNeedHelp as e:
        Log.msg(__doc__)
        Log.msg(" ")
        Log.msg("==================================================")
        Log.msg(" ")
        print(__doc__)
        return 0
        # sys.exit(0) bedeutet, das Programm wurde ordnungsgemaess ausgefuehrt.
    except Exception as e:
        Log.msg(e)
        Log.msg(" ")
        Log.msg("==================================================")
        Log.msg(" ")
        print(e)
        return 2
        # sys.exit(2) bedeutet, der Fehler wurde nicht behandelt und das Programm
        # wird unerwartet abgebrochen.
    else:
        Log.msg(" ")
        Log.msg("==================================================")
        Log.msg(" ")
        return 0
        # sys.exit(0) bedeutet, das Programm wurde ordnungsgemaess ausgefuehrt.


# Einstiegspunkt fuer das Programm.
# mit sys.exit(main()) gibt es nur genau einen Punkt fuer das Programm
# um regulaer zu beenden.
if __name__ == "__main__":
    sys.exit(main())
