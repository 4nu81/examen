from UsrError import UsrError

class FeldBuilder:
    """
    Baut aus den Informationen in der Eingabedatei
    das Spielfeld zusammen. Vorher wurde der Inhalt der Eingabedatei
    nicht geprueft, weshalb das jetzt hier ebenfalls passiert.
    """
    def getFeld(self, filename):
        try:
            # datei oeffnen (mit "r" als Parameter um nur zu lesen)
            Field = []
            f = open(filename, "r")            
        except:
            raise UsrError("Fehler beim oeffnen der Datei %s" % (filename,))

        # bei Erfolg
        else:
            file = []
            # Alle Zeilen aus der Datei in die Collection file schreiben.
            for line in f:
                file.append(line)

            # Die Spielfelddefinition wird initialisiert mit einem leeren String.
            FieldDef = ""

            # existiert mindestens eine Kommentarzeile?
            if not file[0].startswith("#"):
                raise UsrError("In der Eingabedatei soll mindestens eine Kommentarzeile angegeben sein")
            
            for line in file:
                
                # Die erste Zeile in der Datei, die nicht mit "#" beginnt,
                # sollte die Spielfelddefinition enthalten.
                if not line.startswith("#"):
                    FieldDef = line
                    
                    # Folgezeilen werden ignoriert
                    break

            # Falls es keine Zeile gab, die mit "#" anfing oder zwischen den
            # Kommentaren und der Definition eine leerzeile gab, wird eine
            # Fehlerbehandlung mit entsprechender Message erzeugt.
            if FieldDef == "":
                raise UsrError("Keine Startverteilung fuer die Reihen angegeben")

            # Gab es eine nicht leere Zeile wird versucht, darin die Zahlen zu
            # finden, die die Spielfeld-Startbedingungen wiederspiegeln.
            for i in range(len(FieldDef)):
                
                #alle ungeraden sollten ein wert enthalten.
                if i % 2 == 0: # die ungeraden Zahlen (faengt bei 0 an)
                    try:
                        # Versuch der Umwandlung des Zeichens in eine Zahl
                        Field.append(int(FieldDef[i]))
                    except:
                        raise UsrError("Eingabefehler in der Datei %s in Zeile '%s' \n" % (filename, FieldDef,) +
                                        "%s ist keine Ganzzahl"  % (FieldDef[i],)
                                       )
                    # ist eine Null angegeben, ist die Startbedingung ungueltig
                    if FieldDef[i] == "0":
                        raise UsrError("Es duerfen keine Startreihen mit dem Wert '0' uebergeben werden!")

                # geradzahlige Zeichen in der Kette sollen Leerzeichen sein.
                if i % 2 == 1: # die geraden Zahlen
                    if FieldDef[i] != " ":
                        raise UsrError("Eingabefehler in der Datei %s in Zeile '%s'" % (filename, FieldDef,))
                    
                # wurden mehr als 9 Reihen angelegt ist die Felddefinition ebenfalls
                # ungueltig laut Aufgabenstellung
                if len(Field) > 9:
                    raise UsrError("Es wurden zu viele Reihen angegeben. Maximal 9 Reihen sind erlaubt")
                
            else:
                # gab es keine Fehler wird das erzeugte Feld zurueckgegeben
                return Field
