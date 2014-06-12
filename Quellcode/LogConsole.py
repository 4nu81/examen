# -*- coding: utf-8 -*-
"""
Diese Klasse realisiert einen Log (log.txt in Programverzeichnis)
"""

import datetime
from UsrError import UsrError as UE

class LogConsole():
    """
    LogConsole soll wenn verlangt Informationen in die log.txt
    im Programmverzeichnis schreiben.
    """
    def __init__(self, override = False):
        """
        Constructor
        override legt fest ob im Modus "append" oder "override" geschrieben
        werden soll. Standard bei False ist "append"
        """
        try:
            kind = 'a'
            if override:
                kind = 'w'
        except:
            raise UE("Falscher Parameter in Methode uebergeben")

        try:
            # oeffnen der log.txt Datei
            self.f = open('log.txt', kind)
        except:
            print("open Log-File failed")
            self.f = None
            
    
    def msg(self, log_msg):
        """
        msg schreibt den str aus log_msg in die log.txt Datei
        """
        try:
            if not self.f is None:
                msg = str(datetime.datetime.now()) + " : " + str(log_msg) + "\n"
                self.f.write(msg)
        except IOError:
            print("LogMessage failed")

    def msgList(self, List):
        """
        Eine uebergebene Stringliste wird Zeilenweise in die Log geschrieben
        """
        for line in List:
            self.msg(line)
