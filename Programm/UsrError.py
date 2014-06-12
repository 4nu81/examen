class UsrError(Exception):
    """
    Diese Exceptionklasse wird verwendet, wenn der Fehler innerhalb
    meines Programmes abgefangen wurde oder sie wurde erzeugt, um
    eine Fehlerhafte Benutzung anzuzeigen.
    """
    def __init__(self, msg):
        """
        Constructor
        der Parameter msg verlangt die Fehlerbeschreibung als str
        """
        self.msg = msg

class UsrNeedHelp(Exception):
    """
    Diese Exceptionklasse zeigt an, wenn der Benutzer die Hilfe
    angefordert hat.
    """
    def __init__(self):
        Exception.__init__(self)
