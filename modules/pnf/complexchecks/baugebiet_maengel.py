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
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Fehlerarten"
            layer["featuretype"] = "t_maengel_fehler"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = u"Mängel - Bebautes Gebiet" + " (" + project_id + ")"

            layer_fehlerarten = utils.loadLayer(self.iface, layer)    
            if layer_fehlerarten:
                layer_fehlerarten.setLayerName(u"Fehlerarten")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Maengelarten"
            layer["featuretype"] = "t_maengel_art"
            layer["key"] = "ogc_fid"            
            layer["sql"] = "gruppe = 'Bebautes Gebiet'"
            layer["readonly"] = True
            layer["group"] = u"Mängel - Bebautes Gebiet" + " (" + project_id + ")"

            layer_maengelarten = utils.loadLayer(self.iface, layer)    
            if layer_maengelarten:
                layer_maengelarten.setLayerName(u"Mängelarten")

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Maengelliste (Punkte)"
            layer["featuretype"] = "t_maengel"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"
            layer["readonly"] = False
            layer["sql"] = "gruppe = 'Bebautes Gebiet'"                        
            layer["group"] = u"Mängel - Bebautes Gebiet" + " (" + project_id + ")"
            layer["style"] = "maengel/maengel.qml"

            vlayer = utils.loadLayer(self.iface, layer)  
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True) 
                vlayer.setLayerName(u"Mängelliste (Punkte)")

                ogc_fid_idx = vlayer.fieldNameIndex("ogc_fid")
                gruppe_idx = vlayer.fieldNameIndex("gruppe")
                art_idx = vlayer.fieldNameIndex("art")
                fehler_idx = vlayer.fieldNameIndex("fehler")
                feld_idx = vlayer.fieldNameIndex("feldkontrolle")
                lnf_idx = vlayer.fieldNameIndex("lnf")
                terr_idx = vlayer.fieldNameIndex("terrestrisch")
                bemerkung_idx = vlayer.fieldNameIndex("bemerkung")
                datum_idx = vlayer.fieldNameIndex("datum")
            
                vlayer.addAttributeAlias(gruppe_idx, "Gruppe:")
                vlayer.addAttributeAlias(art_idx, "Art:")
                vlayer.addAttributeAlias(fehler_idx, "Fehler:")
                vlayer.addAttributeAlias(feld_idx, "Feldkontrolle:")
                vlayer.addAttributeAlias(lnf_idx, u"Laufende Nachführung:")
                vlayer.addAttributeAlias(terr_idx, "Terrestrische Aufnahme:")
                vlayer.addAttributeAlias(bemerkung_idx, "Bemerkung:")
      
                vlayer.setEditType(ogc_fid_idx, 11)
                vlayer.setEditType(gruppe_idx, 15)
                vlayer.setEditType(art_idx, 15)
                vlayer.setEditType(fehler_idx, 15)
                vlayer.setEditType(feld_idx, 7)
                vlayer.setEditType(lnf_idx, 7)
                vlayer.setEditType(terr_idx, 7)
                vlayer.setEditType(bemerkung_idx, 12)            
                vlayer.setEditType(datum_idx, 11) 

                vlayer.setCheckedState(feld_idx, 't', 'f')
                vlayer.setCheckedState(lnf_idx, 't', 'f')
                vlayer.setCheckedState(terr_idx, 't', 'f')
                
                gruppe_valrel = vlayer.valueRelation(gruppe_idx)
                gruppe_valrel.mLayer = layer_maengelarten.id()
                gruppe_valrel.mKey = "gruppe"
                gruppe_valrel.mValue = "gruppe"
                gruppe_valrel.mOrderByValue = True
                gruppe_valrel.mAllowNull = False
                gruppe_valrel.mAllowMulti = False
                
                art_valrel = vlayer.valueRelation(art_idx)
                art_valrel.mLayer = layer_maengelarten.id()
                art_valrel.mKey = "art_txt"
                art_valrel.mValue = "art_txt"
                art_valrel.mOrderByValue = True
                art_valrel.mAllowNull = True
                art_valrel.mAllowMulti = False
                
                fehler_valrel = vlayer.valueRelation(fehler_idx)
                fehler_valrel.mLayer = layer_fehlerarten.id()
                fehler_valrel.mKey = "fehler_txt"
                fehler_valrel.mValue = "fehler_txt"
                fehler_valrel.mOrderByValue = True
                fehler_valrel.mAllowNull = True
                fehler_valrel.mAllowMulti = False            

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"Maengelliste (Linien)"
            layer["featuretype"] = "t_maengel_linie"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"
            layer["readonly"] = False
            layer["sql"] = "gruppe = 'Bebautes Gebiet'"                        
            layer["group"] = u"Mängel - Bebautes Gebiet" + " (" + project_id + ")"
            layer["style"] = "maengel/maengel_linie.qml"

            vlayer =utils.loadLayer(self.iface, layer)  
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True) 
                vlayer.setLayerName(u"Mängelliste (Linie)")
                    
                ogc_fid_idx = vlayer.fieldNameIndex("ogc_fid")
                gruppe_idx = vlayer.fieldNameIndex("gruppe")
                art_idx = vlayer.fieldNameIndex("art")
                fehler_idx = vlayer.fieldNameIndex("fehler")
                feld_idx = vlayer.fieldNameIndex("feldkontrolle")
                lnf_idx = vlayer.fieldNameIndex("lnf")
                terr_idx = vlayer.fieldNameIndex("terrestrisch")
                bemerkung_idx = vlayer.fieldNameIndex("bemerkung")
                datum_idx = vlayer.fieldNameIndex("datum")
            
                vlayer.addAttributeAlias(gruppe_idx, "Gruppe:")
                vlayer.addAttributeAlias(art_idx, "Art:")
                vlayer.addAttributeAlias(fehler_idx, "Fehler:")
                vlayer.addAttributeAlias(feld_idx, "Feldkontrolle:")
                vlayer.addAttributeAlias(lnf_idx, u"Laufende Nachführung:")
                vlayer.addAttributeAlias(terr_idx, "Terrestrische Aufnahme:")
                vlayer.addAttributeAlias(bemerkung_idx, "Bemerkung:")
      
                vlayer.setEditType(ogc_fid_idx, 11)
                vlayer.setEditType(gruppe_idx, 15)
                vlayer.setEditType(art_idx, 15)
                vlayer.setEditType(fehler_idx, 15)
                vlayer.setEditType(feld_idx, 7)
                vlayer.setEditType(lnf_idx, 7)
                vlayer.setEditType(terr_idx, 7)
                vlayer.setEditType(bemerkung_idx, 12)            
                vlayer.setEditType(datum_idx, 11) 

                vlayer.setCheckedState(feld_idx, 't', 'f')
                vlayer.setCheckedState(lnf_idx, 't', 'f')
                vlayer.setCheckedState(terr_idx, 't', 'f')
                
                gruppe_valrel = vlayer.valueRelation(gruppe_idx)
                gruppe_valrel.mLayer = layer_maengelarten.id()
                gruppe_valrel.mKey = "gruppe"
                gruppe_valrel.mValue = "gruppe"
                gruppe_valrel.mOrderByValue = True
                gruppe_valrel.mAllowNull = False
                gruppe_valrel.mAllowMulti = False
                
                art_valrel = vlayer.valueRelation(art_idx)
                art_valrel.mLayer = layer_maengelarten.id()
                art_valrel.mKey = "art_txt"
                art_valrel.mValue = "art_txt"
                art_valrel.mOrderByValue = True
                art_valrel.mAllowNull = True
                art_valrel.mAllowMulti = False
                
                fehler_valrel = vlayer.valueRelation(fehler_idx)
                fehler_valrel.mLayer = layer_fehlerarten.id()
                fehler_valrel.mKey = "fehler_txt"
                fehler_valrel.mValue = "fehler_txt"
                fehler_valrel.mOrderByValue = True
                fehler_valrel.mAllowNull = True
                fehler_valrel.mAllowMulti = False            
            
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
