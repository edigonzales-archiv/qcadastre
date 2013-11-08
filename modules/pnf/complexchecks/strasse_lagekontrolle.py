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
            group = "Lagekontrolle - Strasse" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "wms"
            layer["title"] = "Orthofoto CIR"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
            layer["layers"] = "Orthofoto11_CIR"
            layer["format"] = "image/jpeg"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            
            rlayer = utils.loadLayer(self.iface, layer)         
            
            layer = {}
            layer["type"] = "wms"
            layer["title"] = "Orthofoto RGB"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
            layer["layers"] = "Orthofoto_SO"
            layer["format"] = "image/jpeg"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            rlayer = utils.loadLayer(self.iface, layer) 
            if rlayer:
                self.iface.legendInterface().setLayerVisible(rlayer, True)     
            
            layer = {}
            layer["type"] = "wms"
            layer["title"] = "Wanderwege"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_wander.wms"
            layer["layers"] = "wweg"
            layer["format"] = "image/png"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            rlayer = utils.loadLayer(self.iface, layer) 
            if rlayer:
               self.iface.legendInterface().setLayerVisible(rlayer, True)                 
        
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
  
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.BoFlaeche"
            layer["featuretype"] = "bodenbedeckung_boflaeche"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_strasse_ortho_massstab.qml"

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
            layer["title"] = u"EO.Punktelement"
            layer["featuretype"] = "v_einzelobjekte_punktelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_pk_andere.qml"

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
            layer["title"] = u"GEB.Strassenstueck"
            layer["featuretype"] = "gebaeudeadressen_strassenstueck"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "geb/strassenstueck.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)  

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "TS-Einteilung"
            layer["featuretype"] = "tseinteilung_toleranzstufe"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "ts/ts_einteilung.qml"
            
            vlayer = utils.loadLayer(self.iface, layer)       

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Kontrollraster (Planeinteilung)"
            layer["featuretype"] = "t_kontrollraster_plan_strasse"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = False
            layer["group"] = group
            layer["style"] = "kontrollraster/kontrollraster.qml"
            
            vlayer = utils.loadLayer(self.iface, layer)       
            if vlayer:            
                self.iface.legendInterface().setLayerVisible(vlayer, False)        
                provider = vlayer.dataProvider()
                ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
                vlayer.setEditType(ogc_fid_idx, 10)
                
                plannummer_idx = provider.fieldNameIndex("plannummer")
                vlayer.setEditType(plannummer_idx, 10)            
                
                kontrolliert_idx = provider.fieldNameIndex("kontrolliert")
                vlayer.setEditType(kontrolliert_idx, 7)
                vlayer.setCheckedState(kontrolliert_idx, 't', 'f')

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Kontrollraster"
            layer["featuretype"] = "t_kontrollraster_strasse_500"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = False
            layer["group"] = group
            layer["style"] = "kontrollraster/kontrollraster.qml"
            
            vlayer = utils.loadLayer(self.iface, layer)       
            if vlayer <> False:            
                self.iface.legendInterface().setLayerVisible(vlayer, True)        
                provider = vlayer.dataProvider()
                ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
    #        vlayer.setEditType(ogc_fid_idx, QgsVectorLayer.EditType.Hidden)
                vlayer.setEditType(ogc_fid_idx, 10)
                
                kontrolliert_idx = provider.fieldNameIndex("kontrolliert")
                vlayer.setEditType(kontrolliert_idx, 7)
                vlayer.setCheckedState(kontrolliert_idx, 't', 'f')

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
