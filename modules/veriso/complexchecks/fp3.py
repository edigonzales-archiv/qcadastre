 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import qcadastre.modules.pnf.tools.utils as utils


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
            group = "FixpunkteKategorie3" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Toleranzstufen"
            layer["featuretype"] = "tseinteilung_toleranzstufe"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "tseinteilung/toleranzstufe.qml"
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"LFP3 Nachfuehrung"
            layer["featuretype"] = "fixpunktekategorie3_lfp3nachfuehrung"
            layer["geom"] = "perimeter"            
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                vlayer.setLayerName(u"LFP3 Nachführung")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "LFP3"
            layer["featuretype"] = "fixpunktekategorie3_lfp3"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "fixpunkte/lfp3.qml"
            
            vlayer = utils.loadLayer(self.iface, layer, True) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "LFP3 ausserhalb Gemeinde"
            layer["featuretype"] = "v_lfp3_ausserhalb_gemeinde"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "fixpunkte/lfp3ausserhalb.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Gemeindegrenze"
            layer["featuretype"] = "gemeindegrenzen_gemeindegrenze"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "gemeindegrenze/gemgre_strichliert.qml"

            gemgrelayer = utils.loadLayer(self.iface, layer, True) 
            if gemgrelayer:
                self.iface.legendInterface().setLayerVisible(gemgrelayer, True)     

            if gemgrelayer:
                rect = gemgrelayer.extent()
                rect.scale(1.2)
                self.iface.mapCanvas().setExtent(rect)        
                self.iface.mapCanvas().refresh() 

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
