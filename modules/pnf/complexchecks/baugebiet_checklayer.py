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
            group = "Checklayer - Bebautes Gebiet" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.Objektname 'u.'"
            layer["featuretype"] = "t_bbobj_u"
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
            layer["title"] = "EO.Objektname 'u.'"
            layer["featuretype"] = "t_eoobj_u"
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
            layer["title"] = "EO.Treppe nicht ein Objekt"
            layer["featuretype"] = "t_treppe_modellbildung"
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
            layer["title"] = u"EO.Flaechenelement 'uebrig. Geb.teil' freistehend"
            layer["featuretype"] = "t_gebteil_frei"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Flächenelement 'übrig. Geb.teil' freistehend")
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Linienelement 'uebrig. Geb.teil' ausserhalb Gebaeude"
            layer["featuretype"] = "t_gebteil_ausserhalb"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Linienelement 'übrig. Geb.teil' ausserhalb Gebäude")                
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Flaechenelement 'uebrig. Geb.teil' innerhalb Gebaeude"
            layer["featuretype"] = "t_gebteil_geb"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Flächenelement 'übrig. Geb.teil' innerhalb Gebäude")                                
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Pfeiler im Gebaeude"
            layer["featuretype"] = "t_pfeiler_gebaeude"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Pfeiler im Gebäude")                                                
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.uebriger_Gebaeudeteil < 1.5 m2"
            layer["featuretype"] = "t_gebteil_15"
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
            layer["title"] = u"Ein EO.Objekt pro Element"
            layer["featuretype"] = "t_eo_modellbildung"
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
            layer["title"] = u"BB.Wasserbecken mit EO.Mauer"
            layer["featuretype"] = "t_mauer_wasserbecken"
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
            layer["title"] = u"EO.Linienelement Mauer"
            layer["featuretype"] = "t_mauer_linien"
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
            layer["title"] = u"EO.Linienelement Mauer ausserhalb EO.Flaechenelement Mauer"
            layer["featuretype"] = "t_mauer_ausserhalb"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Linienelement Mauer ausserhalb EO.Flächenelement Mauer")                                                                
                self.iface.legendInterface().setLayerVisible(vlayer, True)    
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Mauer freistehend"
            layer["featuretype"] = "t_mauer_freistehend"
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
            layer["title"] = "EO.Mauer nicht ein Objekt"
            layer["featuretype"] = "t_mauer_modellbildung"
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
            layer["title"] = u"BB.Gebaeude ohne Gartenanlage"
            layer["featuretype"] = "t_abgrenzung_gartenanlage"
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
            layer["title"] = u"BB.Gebaeude ohne Erschliessung"
            layer["featuretype"] = "t_geb_ohne_ersch"
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
            layer["title"] = u"BB.Parkplatz < 100 m2"
            layer["featuretype"] = "t_pp_kleiner_100"
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
            layer["title"] = u"BB.Gebaeude mit mehreren Adressen"
            layer["featuretype"] = "t_2_gebein"
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
            layer["title"] = u"BB.Gebaeude < 6 m2"
            layer["featuretype"] = "t_gebaeude_kleiner_6"
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
            layer["title"] = u"EO.Linienelement unterird. Gebaeude"
            layer["featuretype"] = "t_u_geb_linien"
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
            layer["title"] = u"EO.Unterstand auf Gebaeude"
            layer["featuretype"] = "t_unterstand_auf_geb"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                vlayer.setLayerName(u"EO.Unterstand auf Gebäude")                                                                                
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

        except Exception, e:
            QApplication.restoreOverrideCursor       
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
        QApplication.restoreOverrideCursor()        

        try:
            self.canvas.setMapUnits(0)		
            srs = QgsCoordinateReferenceSystem()
            srs.createFromSrid(int(epsg))
            renderer = self.canvas.mapRenderer()
            renderer.setDestinationCrs(srs)
        except Exception, e:
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
