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
            group = "Checklayer - Strasse" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.BoFlaeche"
            layer["featuretype"] = "bodenbedeckung_boflaeche"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_strasse_bbplan.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Flaechenelement"
            layer["featuretype"] = "v_einzelobjekte_flaechenelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_fl_strasse_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Linienelement"
            layer["featuretype"] = "v_einzelobjekte_linienelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_li_strasse_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"LI.Liegenschaft"
            layer["featuretype"] = "liegenschaften_liegenschaft"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "li/liegenschaft_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, False)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Pfeiler < 0.25 m2"
            layer["featuretype"] = "t_pfeiler_50cm"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"
            
            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:            
                self.iface.legendInterface().setLayerVisible(vlayer, True)        

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.Strasse_Weg > 10000 m2"
            layer["featuretype"] = "t_str_flaeche_10000"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"
            
            vlayer = utils.loadLayer(self.iface, layer)       
            if vlayer:            
                self.iface.legendInterface().setLayerVisible(vlayer, True)  

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.schmaler_Weg in TS 2"
            layer["featuretype"] = "t_schmaler_weg_ts2"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"
            
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
