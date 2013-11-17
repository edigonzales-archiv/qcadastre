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
            group = "Gebaeudeadressen - Lokalisationstest" + " (" + str(project_id) + ")"
        
            vlayer_lokalisation = self.getVectorLayerByName("Lokalisation Lokalisationstest")
            
            if vlayer_lokalisation == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Lokalisation Lokalisationstest"
                layer["featuretype"] = "gebaeudeadressen_lokalisation"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "tid = '-1'"
                layer["readonly"] = True
                layer["group"] = group
                
                vlayer_lokalisation = utils.loadLayer(self.iface, layer, True) 

            vlayer_strassenstueck_geometrie = self.getVectorLayerByName("Strassenstueck (geometrie) Lokalisationstest")
            
            if vlayer_strassenstueck_geometrie == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Strassenstueck (geometrie) Lokalisationstest"
                layer["featuretype"] = "gebaeudeadressen_strassenstueck"
                layer["geom"] = "geometrie"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "strassenstueck_von = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/strassenachsen_rot.qml"
                vlayer_strassenstueck_geometrie =  utils.loadLayer(self.iface, layer, False) 

                if vlayer_strassenstueck_geometrie:
                    self.iface.legendInterface().setLayerVisible(vlayer_strassenstueck_geometrie, True)                     

            vlayer_strassenstueck_anfangspunkt = self.getVectorLayerByName("Strassenstueck (anfangspunkt) Lokalisationstest")

            if vlayer_strassenstueck_anfangspunkt == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Strassenstueck (anfangspunkt) Lokalisationstest"
                layer["featuretype"] = "gebaeudeadressen_strassenstueck"
                layer["geom"] = "anfangspunkt"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "strassenstueck_von = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/anfangspunkt_rot.qml"
                vlayer_strassenstueck_anfangspunkt =  utils.loadLayer(self.iface, layer, False) 

                if vlayer_strassenstueck_anfangspunkt:
                    self.iface.legendInterface().setLayerVisible(vlayer_strassenstueck_anfangspunkt, True)                     

            vlayer_benanntesgebiet = self.getVectorLayerByName("Benanntes Gebiet Lokalisationstest")

            if vlayer_benanntesgebiet == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Benanntes Gebiet Lokalisationstest"
                layer["featuretype"] = "gebaeudeadressen_benanntesgebiet"
                layer["geom"] = "flaeche"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "benanntesgebiet_von = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/benanntesgebiet_rot.qml"
                vlayer_benanntesgebiet =  utils.loadLayer(self.iface, layer, False) 

                if vlayer_benanntesgebiet:
                    self.iface.legendInterface().setLayerVisible(vlayer_benanntesgebiet, True)                     

            vlayer_gebaeudeeingang = self.getVectorLayerByName("Gebaeudeeingang Lokalisationstest")

            if vlayer_gebaeudeeingang == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Gebaeudeeingang Lokalisationstest"
                layer["featuretype"] = "gebaeudeadressen_gebaeudeeingang"
                layer["geom"] = "lage"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "gebaeudeeingang_von = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/gebaeudeeingang_rot.qml"
                vlayer_gebaeudeeingang =  utils.loadLayer(self.iface, layer, False) 

                if vlayer_gebaeudeeingang:
                    self.iface.legendInterface().setLayerVisible(vlayer_gebaeudeeingang, True)                     

            vlayer_shortestline = self.getVectorLayerByName("Kuerzeste Linie Lokalisationstest")

            if vlayer_shortestline == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "Kuerzeste Linie Lokalisationstest"
                layer["featuretype"] = "t_shortestline_hausnummerpos"
                layer["geom"] = "the_geom"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "lok_tid = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/shortestline_linie_rot.qml"
                vlayer_shortestline =  utils.loadLayer(self.iface, layer, False) 

                if vlayer_shortestline:
                    self.iface.legendInterface().setLayerVisible(vlayer_shortestline, True)                     

            vlayer_hausnummerpos = self.getVectorLayerByName("HausnummerPos Lokalisationstest")

            if vlayer_hausnummerpos == None:
                layer = {}
                layer["type"] = "postgres"
                layer["title"] = "HausnummerPos Lokalisationstest"
                layer["featuretype"] = "v_gebaeudeadressen_hausnummerpos"
                layer["geom"] = "pos"
                layer["key"] = "ogc_fid"            
                layer["sql"] = "lok_tid = '-1'"
                layer["readonly"] = True                
                layer["group"] = group
                layer["style"] = "gebaeudeadressen/hausnummerpos_rot.qml"
                vlayer_hausnummerpos =  utils.loadLayer(self.iface, layer, True) 

                if vlayer_hausnummerpos:
                    self.iface.legendInterface().setLayerVisible(vlayer_hausnummerpos, True)                     


            vlayer_lokalisationsname = self.getVectorLayerByName("LokalisationsName")
            if vlayer_lokalisationsname == None:
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Layer 'LokalisationsName' not found."), level=QgsMessageBar.CRITICAL)                    
                QApplication.restoreOverrideCursor()   
                return         

            iter = vlayer_lokalisationsname.getFeatures()
            ids = []

            for feature in iter:
                ids.append(feature.id())

            if vlayer_lokalisationsname.selectedFeatureCount() < 1:
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "No 'LokalisationsName' selected."), level=QgsMessageBar.CRITICAL)                    
                QApplication.restoreOverrideCursor()   
                return         
                
            if vlayer_lokalisationsname.selectedFeatureCount() > 1:
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Please select only one 'LokalisationsName'."), level=QgsMessageBar.CRITICAL)                    
                QApplication.restoreOverrideCursor()   
                return         

            feat = QgsFeature()
            id = vlayer_lokalisationsname.selectedFeaturesIds()[0]            
            feat = vlayer_lokalisationsname.selectedFeatures()[0]
            idx = ids.index(id)
            
            benannte_idx = vlayer_lokalisationsname.fieldNameIndex("benannte")
            text_idx = vlayer_lokalisationsname.fieldNameIndex("text")
            
            if benannte_idx == -1 or text_idx == -1:
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Field not found."), level=QgsMessageBar.CRITICAL)                    
                QApplication.restoreOverrideCursor()
                return

            benannte =  feat.attributes()[benannte_idx]
            lokalisationsname = feat.attributes()[text_idx]
        
            vlayer_strassenstueck_geometrie.setSubsetString("(strassenstueck_von = '"+benannte+"')")
            vlayer_strassenstueck_anfangspunkt.setSubsetString("(strassenstueck_von = '"+benannte+"')")
            vlayer_benanntesgebiet.setSubsetString("(benanntesgebiet_von = '"+benannte+"')")
            vlayer_gebaeudeeingang.setSubsetString("(gebaeudeeingang_von = '"+benannte+"')")
            vlayer_lokalisation.setSubsetString("(tid = '"+benannte+"')")
            vlayer_shortestline.setSubsetString("(lok_tid = '"+benannte+"')")
            vlayer_hausnummerpos.setSubsetString("(lok_tid = '"+benannte+"')")

            if vlayer_strassenstueck_geometrie.featureCount() > 0:
                xMin = vlayer_strassenstueck_geometrie.extent().xMinimum()
                yMin = vlayer_strassenstueck_geometrie.extent().yMinimum()
                xMax = vlayer_strassenstueck_geometrie.extent().xMaximum()
                yMax = vlayer_strassenstueck_geometrie.extent().yMaximum()
                
            if vlayer_benanntesgebiet.featureCount() > 0:
                xMin = vlayer_benanntesgebiet.extent().xMinimum()
                yMin = vlayer_benanntesgebiet.extent().yMinimum()
                xMax = vlayer_benanntesgebiet.extent().xMaximum()
                yMax = vlayer_benanntesgebiet.extent().yMaximum()
               
            try:
                if vlayer_gebaeudeeingang.featureCount() > 0:
                    if vlayer_gebaeudeeingang.extent().xMinimum() < xMin:
                        xMin = vlayer_gebaeudeeingang.extent().xMinimum()
                    if vlayer_gebaeudeeingang.extent().yMinimum() < yMin:
                        yMin = vlayer_gebaeudeeingang.extent().yMinimum()
                    if vlayer_gebaeudeeingang.extent().xMaximum() > xMax:
                        xMax = vlayer_gebaeudeeingang.extent().xMaximum()
                    if vlayer_gebaeudeeingang.extent().yMaximum() > yMax:
                        yMax = vlayer_gebaeudeeingang.extent().yMaximum()                
                        
                rect = QgsRectangle(xMin,  yMin,  xMax,  yMax)
                rect.scale(1.3)
        
            except UnboundLocalError, e:
                print "Couldn't do it: %s" % e                            
                vlayer_gemeindegrenze = self.getVectorLayerByName("Gemeindegrenze")
                if vlayer_gemeindegrenze == None:
                    rect = self.canvas.fullExtent()
                else:
                    rect = vlayer_gemeindegrenze.extent()

            self.iface.mapCanvas().setExtent(rect)
            self.iface.mapCanvas().refresh()                
            
            iter = vlayer_lokalisation.getFeatures()
            
            # only one feature is selected
            for feature in iter:
                print feature
                prinzip_idx = vlayer_lokalisation.fieldNameIndex("nummerierungsprinzip_txt")
                attributeprovisorisch_idx = vlayer_lokalisation.fieldNameIndex("attributeprovisorisch_txt")
                offiziell_idx = vlayer_lokalisation.fieldNameIndex("istoffiziellebezeichnung_txt")
                status_idx = vlayer_lokalisation.fieldNameIndex("status_txt")
                inaenderung_idx = vlayer_lokalisation.fieldNameIndex("inaenderung_txt")
                art_idx = vlayer_lokalisation.fieldNameIndex("art_txt")
                
                if prinzip_idx == -1 or attributeprovisorisch_idx == -1 or offiziell_idx == -1 or status_idx == -1 or inaenderung_idx == -1 or art_idx == -1:
                    self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Field not found."), level=QgsMessageBar.CRITICAL)                    
                    QApplication.restoreOverrideCursor()
                    return

                prinzip = feature.attributes()[prinzip_idx]
                attributeprovisorisch = feature.attributes()[attributeprovisorisch_idx]            
                offiziell = feature.attributes()[offiziell_idx]
                status = feature.attributes()[status_idx]
                inaenderung = feature.attributes()[inaenderung_idx]
                art = feature.attributes()[art_idx]

                map_extent = self.canvas.extent()
                x = map_extent.xMinimum()
                y = map_extent.yMaximum()

            text_item_found = False
            items = self.iface.mapCanvas().scene().items()
            print items
            for i in range (len(items)):
                try:
                    name =  items[i].data(0)
                    if name.toString() == "LokalisationsInfo":
                        text_item = items[i]
                        text_item_found = True
                except Exception, e:
                    pass
#                    print "Couldn't do it: %s" % e            
            
            if not text_item_found:
                text_item = QgsTextAnnotationItem(self.canvas)
                text_item.setData(0, "LokalisationsInfo")

            text_item.setMapPosition(QgsPoint(x+10*self.canvas.mapUnitsPerPixel(), y-10*self.canvas.mapUnitsPerPixel()))
            text_item.setMapPositionFixed(False)
            text_item.setFrameBorderWidth(0.0)   
            text_item.setFrameColor(QColor(250, 250, 250, 255))
            text_item.setFrameBackgroundColor(QColor(250, 250, 250, 255))
            text_item.setFrameSize(QSizeF(250,150))
            text_document = QTextDocument()
            text_document.setHtml("<table style='font-size:12px;'><tr><td>Lok.Name: </td><td>"+lokalisationsname+"</td></tr><tr><td>TID: </td><td>"+benannte+"</td></tr> <tr><td>Num.prinzip: </td><td>"+prinzip+"</td></tr> <tr><td>Attr. prov.: </td><td>"+attributeprovisorisch+"</td></tr> <tr><td>ist offiziell: </td><td>"+offiziell+"</td></tr> <tr><td>Status: </td><td>"+status+"</td></tr> <tr><td>in Aenderung: </td><td>"+inaenderung+"</td></tr> <tr><td>Art: </td><td>"+art+"</td></tr>  </table>")
            text_item.setDocument(text_document)
            
#            text_item.update()        
#            self.iface.mapCanvas().refresh()          
            
            # Workaround: das erste Mal passt die Position nicht...???
            text_item.setMapPosition(QgsPoint(x+10*self.canvas.mapUnitsPerPixel(), y-10*self.canvas.mapUnitsPerPixel()))        
            text_item.update()               

            self.iface.mapCanvas().refresh()          

            try:
                vlayer_lokalisationsname.setSelectedFeatures([ids[idx+1]])
            except IndexError:
                self.iface.messageBar().pushMessage("Information",  QCoreApplication.translate("QcadastreModule", "End of table."), level=QgsMessageBar.INFO)                    

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

    # Return QgsVectorLayer from a layer name ( as string )
    # (c) Carson Farmer / fTools
    def getVectorLayerByName(self, myName):
        layermap = QgsMapLayerRegistry.instance().mapLayers()
        for name, layer in layermap.iteritems():
            if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
                if layer.isValid():
                    return layer
                else:
                    return None 
