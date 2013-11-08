 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface

    def run(self):        
        try:  
            _temp = __import__("baugebiet_maengel", globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()
         
            _temp = __import__("baugebiet_checklayer", globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()    
    
            _temp = __import__("baugebiet_lagekontrolle", globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()
            
        except Exception, e:
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    



