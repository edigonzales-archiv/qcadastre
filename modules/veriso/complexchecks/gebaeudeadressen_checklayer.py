 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import qcadastre.modules.veriso.tools.utils as utils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
    def run(self):        
        self.settings = QSettings("CatAIS","Qcadastre")
        project_id = (self.settings.value("project/id"))
        epsg = (self.settings.value("project/epsg"))
        
        if not project_id:
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
            return
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = "Gebaeudeadressen - Checklayer" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Spinnennetz"
            layer["featuretype"] = "t_gebaeudeadressen_spinnennetz"
            layer["geom"] = "line"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/spinnennetz_blau.qml"
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Kuerzeste Linie"
            layer["featuretype"] = "t_shortestline_hausnummerpos"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/shortestline_linie.qml"
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Kürzeste Linie (HausnummerPos)")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "HausnummerPos"
            layer["featuretype"] = "v_gebaeudeadressen_hausnummerpos"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/shortestline_hausnummerpos.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     



        except Exception, e:
            QApplication.restoreOverrideCursor()            
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
        QApplication.restoreOverrideCursor()        

        # Workaround for geometryless-tables-wgs84-bug.
        try:
            self.canvas.setMapUnits(0)		
            srs = QgsCoordinateReferenceSystem()
            srs.createFromSrid(int(epsg))
            renderer = self.canvas.mapRenderer()
            renderer.setDestinationCrs(srs)
        except Exception, e:
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
