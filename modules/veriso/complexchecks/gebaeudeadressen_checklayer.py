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
            layer["title"] = u"EO.Flaechenelemente"
            layer["featuretype"] = "v_einzelobjekte_flaechenelement"
            layer["geom"] = "geometrie"            
            layer["key"] = "ogc_fid"            
            layer["sql"] = "art_txt LIKE 'unterirdisches_Gebaeude%' OR art_txt LIKE 'uebriger_Gebaeudeteil%' OR art_txt LIKE 'Reservoir%' OR art_txt LIKE 'Unterstand%'"
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "einzelobjekte/eo_flaeche_gebdetail_unterstand_reservoir_unterirdisch.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)                     
                vlayer.setLayerName(u"EO.Flächenelemente")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Linienelemente"
            layer["featuretype"] = "v_einzelobjekte_linienelement"
            layer["geom"] = "geometrie"            
            layer["key"] = "ogc_fid"            
            layer["sql"] = "art_txt LIKE 'uebriger_Gebaeudeteil%'"
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "einzelobjekte/eo_linie_gebdetail.qml"
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"GEB.Nachfuehrung"
            layer["featuretype"] = "gebaeudeadressen_gebnachfuehrung"
#            layer["geom"] = "perimeter"            
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
#            layer["style"] = "gebaeudeadressen/nf_perimeter.qml"            
            
            vlayer = utils.loadLayer(self.iface, layer)             
            if vlayer:
                vlayer.setLayerName(u"GEB.Nachführung")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Benanntes Gebiet"
            layer["featuretype"] = "gebaeudeadressen_benanntesgebiet"
            layer["geom"] = "flaeche"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True            
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/benanntesgebiet_gruen.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Strassenstueck (geometrie)"
            layer["featuretype"] = "gebaeudeadressen_strassenstueck"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/strassenachsen_gruen.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Strassenstueck (anfangspunkt)"
            layer["featuretype"] = "gebaeudeadressen_strassenstueck"
            layer["geom"] = "anfangspunkt"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/anfangspunkt_gruen.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Gebaeudeeingang"
            layer["featuretype"] = "gebaeudeadressen_gebaeudeeingang"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/gebaeudeeingang_blaues_viereck_mit_label.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "HausnummerPos"
            layer["featuretype"] = "v_gebaeudeadressen_hausnummerpos"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/hausnummerpos.qml"

            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "LokalisationsName"
            layer["featuretype"] = "gebaeudeadressen_lokalisationsname"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            
            vlayer = utils.loadLayer(self.iface, layer) 
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "LokalisationsNamePos"
            layer["featuretype"] = "v_gebaeudeadressen_lokalisationsnamepos"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/lokalisationsnamepos.qml"
            
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

            gemgrelayer = utils.loadLayer(self.iface, layer) 
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
