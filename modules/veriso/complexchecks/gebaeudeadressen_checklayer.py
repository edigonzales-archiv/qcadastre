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
            
            vlayer = utils.loadLayer(self.iface, layer, False) 
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
            
            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, False)     
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

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, False)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeingaenge ohne Lokalisation"
            layer["featuretype"] = "gebaeudeadressen_gebaeudeeingang"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = "gebaeudeeingang_von IS NULL"
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingaenge_ohne_lokalisation.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge ohne Lokalisation")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"LokalisationsName ohne Eingaenge"
            layer["featuretype"] = "v_gebaeudeadressen_lokalisationsname_ohne_gebaeudeeingaenge"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            
            vlayer = utils.loadLayer(self.iface, layer) 
            if vlayer:
                vlayer.setLayerName(u"LokalisationsName ohne Eingänge")
          
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeude > 12m2 ohne Eingang"
            layer["featuretype"] = "t_gebaeude_groesser_12m2_ohne_eingang"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/gebaeude_12m2_ohne_eingang.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäude > 12m2 ohne Eingang")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Strassenstueck istAchse = nein"
            layer["featuretype"] = "gebaeudeadressen_strassenstueck"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = "istachse = 1"
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/strassenachsen_istachse.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge MIT Nummer (falsche Attribute)"
            layer["featuretype"] = "v_gebaeudeadressen_gebaeudeeingang_mit_nummer_attribute"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingange_mit_nummer_falsche_attribute.qml"
            
            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge MIT Nummer (falsche Attribute)")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge OHNE Nummer (falsche Attribute)"
            layer["featuretype"] = "v_gebaeudeadressen_gebaeudeeingang_ohne_nummer_attribute"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingange_ohne_nummer_falsche_attribute.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge OHNE Nummer (falsche Attribute)")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge ausserhalb"
            layer["featuretype"] = "t_gebaeudeadressen_gebaeudeeingang_ausserhalb"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingaenge_ausserhalb.qml"
            
            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge ausserhalb")
           
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge innerhalb Zentroidbuffer"
            layer["featuretype"] = "t_gebaeudeadressen_gebaeudeeingang_innerhalb_centroidbuffer"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingaenge_innerhalb_zentroidbuffer.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge innerhalb Zentroidbuffer")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"HausnummerPos ausserhalb"
            layer["featuretype"] = "t_gebaeudeadressen_hausnummerpos_ausserhalb"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/hausnummerpos_ausserhalb.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"HausnummerPos ohne Nummer"
            layer["featuretype"] = "v_gebaeudeadressen_hausnummerpos_ohne_nummer"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/nummerpos_ohne_nummer.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"HausnummerPos doppelt"
            layer["featuretype"] = "t_gebaeudeadressen_hausnummerpos_doppelt"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/nummerpos_doppelt.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge mit Nummer ohne Position"
            layer["featuretype"] = "t_gebaeudeadressen_gebaeudeeingang_mit_nummer_ohne_pos"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingang_mit_nummer_ohne_position.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge mit Nummer ohne Position")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Gebaeudeeingaenge mit gleicher Nummer zu Lokalisation"
            layer["featuretype"] = "t_gebaeudeadressen_gebaeudeeingang_gleiche_nummer_und_lok"
            layer["geom"] = "lage"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["group"] = group
            layer["style"] = "gebaeudeadressen/eingang_gleiche_nummer_lokalisation.qml"

            vlayer = utils.loadLayer(self.iface, layer, False) 
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)     
                vlayer.setLayerName(u"Gebäudeeingänge mit gleicher Nummer zu Lokalisation")


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
