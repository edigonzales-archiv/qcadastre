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
            group = "Lagekontrolle - Bebautes Gebiet" + " (" + str(project_id) + ")"
        
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
            layer["title"] = "GEWISSO"
            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_gewaesser.wms"
            layer["layers"] = "gewaesser"
            layer["format"] = "image/png"
            layer["crs"] = "EPSG:21781"
            layer["group"] = group
            layer["style"] = "gewaesser/gewisso.qml"    
            
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
            layer["style"] = "bb/bb_baugebiet_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Einzelobjekt"
            layer["featuretype"] = "einzelobjekte_einzelobjekt"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
            layer["group"] = group

            eoeolayer = utils.loadLayer(self.iface, layer)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Flaechenelement"
            layer["featuretype"] = "einzelobjekte_flaechenelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_fl_baugebiet_ortho.qml"

            eoflayer = utils.loadLayer(self.iface, layer)    
            if eoflayer:
                self.iface.legendInterface().setLayerVisible(eoflayer, True)    
                
            if eoeolayer and eoflayer:
                joinLayerId = eoeolayer.id()
                joinProvider = eoeolayer.dataProvider()
                joinIdx = joinProvider.fieldNameIndex("tid")
                
                targetProvider = eoflayer.dataProvider()
                targetIdx = targetProvider.fieldNameIndex("flaechenelement_von")

                joinInfo = QgsVectorJoinInfo()
                joinInfo.joinField = joinIdx
                joinInfo.joinLayerId = joinLayerId
                joinInfo.targetField = targetIdx
                joinInfo.memoryCache = True
                
                eoflayer.addJoin(joinInfo)

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Linienelement"
            layer["featuretype"] = "einzelobjekte_linienelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_li_baugebiet_ortho.qml"

            eolilayer = utils.loadLayer(self.iface, layer)    
            if eolilayer:
                self.iface.legendInterface().setLayerVisible(eolilayer, True)    

            if eoeolayer and eolilayer:
                joinLayerId = eoeolayer.id()
                joinProvider = eoeolayer.dataProvider()
                joinIdx = joinProvider.fieldNameIndex("tid")
                
                targetProvider = eolilayer.dataProvider()
                targetIdx = targetProvider.fieldNameIndex("linienelement_von")
            
                print "**********************"
                print joinIdx
                print targetIdx


                joinInfo = QgsVectorJoinInfo()
                joinInfo.joinField = joinIdx
                joinInfo.joinLayerId = joinLayerId
                joinInfo.targetField = targetIdx
                joinInfo.memoryCache = True
                
                eolilayer.addJoin(joinInfo)

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Punktelement"
            layer["featuretype"] = "einzelobjekte_punktelement"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_pk_andere.qml"

            eopklayer = utils.loadLayer(self.iface, layer)    
            if eopklayer:
                self.iface.legendInterface().setLayerVisible(eopklayer, True)    

            if eoeolayer and eopklayer:
                joinLayerId = eoeolayer.id()
                joinProvider = eoeolayer.dataProvider()
                joinIdx = joinProvider.fieldNameIndex("tid")
                
                targetProvider = eopklayer.dataProvider()
                targetIdx = targetProvider.fieldNameIndex("punktelement_von")

                joinInfo = QgsVectorJoinInfo()
                joinInfo.joinField = joinIdx
                joinInfo.joinLayerId = joinLayerId
                joinInfo.targetField = targetIdx
                joinInfo.memoryCache = True
                
                eopklayer.addJoin(joinInfo)

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
            layer["title"] = u"BB.Objektname"
            layer["featuretype"] = "v_bb_objektnamen"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_objektnamen.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = u"EO.Objektname"
            layer["featuretype"] = "v_eo_objektnamen"
            layer["geom"] = "pos"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "eo/eo_objektnamen.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    

#        layer = {}
#        layer["type"] = "postgres"
#        layer["title"] = u"Reservoir (AfU)"
#        layer["featuretype"] = "reservoir_afu"
#        layer["geom"] = "geom"
#        layer["key"] = "gid"            
#        layer["sql"] = ""
#        layer["readonly"] = True
#        layer["group"] = group
#        layer["style"] = "sogis/reservoir_afu.qml"
#         
#        params =  {}
#        params["appmodule"] = str(self.settings.value("project/active/appmodule").toString())
#        params["subappmodule"] = str(self.settings.value("project/active/subappmodule").toString())      
#        params["provider"] = "postgres"
#        params["dbhost"] = str(self.settings.value("project/active/dbhost").toString())
#        params["dbport"] = str(self.settings.value("project/active/dbport").toString())
#        params["dbname"] = "pnf_varia"
#        params["dbschema"] = "sogis"
#        params["dbuser"] = str(self.settings.value("project/active/dbuser").toString())
#        params["dbpwd"] = str(self.settings.value("project/active/dbpwd").toString())
#        params["dbadmin"] = str(self.settings.value("project/active/dbadmin").toString())
#        params["dbadminpwd"] = str(self.settings.value("project/active/dbadminpwd").toString())
#        
#        layer["params"] = params
#
#        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
#        if vlayer <> False:
#            self.iface.legendInterface().setLayerVisible(vlayer, True)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "Kontrollraster (Planeinteilung)"
            layer["featuretype"] = "t_kontrollraster_plan_bebaut"
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
            if vlayer:            
                self.iface.legendInterface().setLayerVisible(vlayer, True)        
                provider = vlayer.dataProvider()
                ogc_fid_idx = provider.fieldNameIndex("ogc_fid")
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

