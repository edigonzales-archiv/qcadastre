 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *

import os
import xlwt as pycel
import qcadastre.modules.pnf.tools.utils as utils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
    
    def run(self):        
        self.settings = QSettings("CatAIS","Qcadastre")
        project_id = (self.settings.value("project/id"))
        epsg = (self.settings.value("project/epsg"))
        projectdir = (self.settings.value("project/projectdir"))        
        dbhost = (self.settings.value("project/dbhost"))
        dbport = (self.settings.value("project/dbport"))
        dbname = (self.settings.value("project/dbname"))
        dbschema = (self.settings.value("project/dbschema"))
        dbuser = (self.settings.value("project/dbuser"))
        dbpwd = (self.settings.value("project/dbpwd"))        

        if not project_id:
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
            return
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = u"Checklayer - Seltene Objekte" + " (" + str(project_id) + ")"
        
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.BoFlaeche"
            layer["featuretype"] = "bodenbedeckung_boflaeche"
            layer["geom"] = "geometrie"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = True
            layer["group"] = group
            layer["style"] = "bb/bb_bb_plan.qml"

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
            layer["style"] = "eo/eo_fl_bb_plan.qml"

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
            layer["style"] = "eo/eo_li_bb_plan.qml"

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
            layer["readonly"] = "true"
            layer["group"] = group
            layer["style"] = "li/liegenschaft_ortho.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, False)    

            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "BB.Boeschungsbauwerk"
            layer["featuretype"] = "t_boeschungbwerke"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
            layer["group"] = group
            layer["style"] = "checks/checklayer_punkt.qml"

            vlayer = utils.loadLayer(self.iface, layer)    
            if vlayer:
                self.iface.legendInterface().setLayerVisible(vlayer, True)    
            
            layer = {}
            layer["type"] = "postgres"
            layer["title"] = "EO.Brunnen"
            layer["featuretype"] = "t_brunnen"
            layer["geom"] = "the_geom"
            layer["key"] = "ogc_fid"            
            layer["sql"] = ""
            layer["readonly"] = "true"
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

        try:
            self.canvas.setMapUnits(0)		
            srs = QgsCoordinateReferenceSystem()
            srs.createFromSrid(int(epsg))
            renderer = self.canvas.mapRenderer()
            renderer.setDestinationCrs(srs)
        except Exception, e:
            print "Couldn't do it: %s" % e            
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    

        # Export feature count in excel file.
        try:
            db = QSqlDatabase.addDatabase("QPSQL", "SelteneObjekte")
            db.setDatabaseName(dbname)
            db.setHostName(dbhost)
            db.setUserName(dbuser)
            db.setPassword(dbpwd)
            
            if  db.open() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Could not open database:\n") + str(db.lastError().driverText()))            
                return 

            # Create excel file.
            wb = pycel.Workbook(encoding='utf-8')
            wb.country_code = 41
            
            style1 = pycel.easyxf('font: bold on;');
            style2 = pycel.easyxf('font: italic on;');

            # Bodenbedeckung            
            sql = """SELECT CASE WHEN anz IS NULL THEN 0 ELSE anz END, bb_art.code as art, bb_art.code_txt as art_txt
FROM
(
 SELECT count(art) as anz, art_txt, art
 FROM """+dbschema+""".bodenbedeckung_boflaeche
 WHERE art IN (7, 9, 19, 20, 21, 22, 30, 33, 35, 36, 37, 38, 39, 40)
 GROUP BY art, art_txt
) bb
FULL JOIN """+dbschema+""".enum__bodenbedeckung_bbart bb_art ON bb_art.code = bb.art
WHERE bb_art.code IN (7, 9, 19, 20, 21, 22, 30, 33, 35, 36, 37, 38, 39, 40)
ORDER BY bb_art.code;"""

            query = db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while fetching data informations."))            
                return 
                        
            ws = wb.add_sheet(u'BB seltene Objekte')
            ws.paper_size_code = 8
            ws.print_centered_vert = False
            ws.print_centered_horz = False
            ws.top_margin = 1.0
            ws.left_margin = 1.0 
            ws.bottom_margin = 1.0
            ws.portrait = True
            
            ws.write(0, 0,  str("BB seltene Objekte: "), style1 )
            ws.write(0, 1,  project_id)        

            ws.write(2, 0, str("Art"))
            ws.write(2, 1, str("Art-Text"))
            ws.write(2, 2, str("Anzahl"))

            i = 0
            record = query.record()
            while query.next():
                anz = str(query.value(record.indexOf("anz")))
                art = str(query.value(record.indexOf("art")))
                art_txt = str(query.value(record.indexOf("art_txt")))
                
                ws.write(3+i, 0, art)
                ws.write(3+i, 1, art_txt)
                ws.write(3+i, 2, anz)
                
                i += 1

            # Einzelobjekte
            sql = """SELECT CASE WHEN anz IS NULL THEN 0 ELSE anz END, eo_art.code as art, eo_art.code_txt as art_txt
FROM
(
 SELECT count(art) as anz, art_txt, art
 FROM """+dbschema+""".einzelobjekte_einzelobjekt
 WHERE art IN (9, 14, 15, 16, 17, 18, 23, 30, 31, 35, 36, 37, 38, 40, 42)
 GROUP BY art, art_txt
) eo
FULL JOIN """+dbschema+""".enum__einzelobjekte_eoart eo_art ON eo_art.code = eo.art
WHERE eo_art.code IN (9, 14, 15, 16, 17, 18, 23, 30, 31, 35, 36, 37, 38, 40, 42)
ORDER BY eo_art.code"""

            query = db.exec_(sql)
            
            if query.isActive() == False:
                QMessageBox.critical(None,  "QGeoApp", QCoreApplication.translate("QGeoApp", "Error occured while fetching data informations."))            
                return 

            ws = wb.add_sheet(u'EO seltene Objekte')
            ws.paper_size_code = 8
            ws.print_centered_vert = False
            ws.print_centered_horz = False
            ws.top_margin = 1.0
            ws.left_margin = 1.0 
            ws.bottom_margin = 1.0
            ws.portrait = True
            
            ws.write(0, 0,  str("EO seltene Objekte: "), style1)
            ws.write(0, 1,  project_id)        

            ws.write(2, 0, str("Art"))
            ws.write(2, 1, str("Art-Text"))
            ws.write(2, 2, str("Anzahl"))

            i = 0
            record = query.record()
            while query.next():
                anz = str(query.value(record.indexOf("anz")))
                art = str(query.value(record.indexOf("art")))
                art_txt = str(query.value(record.indexOf("art_txt")))
                
                ws.write(3+i, 0, art)
                ws.write(3+i, 1, art_txt)
                if int(anz) > 0:
                    ws.write(3+i, 2, anz, style1)
                else:
                    ws.write(3+i, 2, anz)
                
                i += 1

            file = QDir.convertSeparators(QDir.cleanPath(projectdir + os.sep + "seltene_objekte.xls"))
            try:
                wb.save(file)
                self.iface.messageBar().pushMessage("Information",  QCoreApplication.translate("QcadastreModule", "File written:\n") + file, level=QgsMessageBar.INFO, duration=5)                    
            except IOError:
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "File <b>not</b> written!\n") + file, level=QgsMessageBar.CRITICAL, duration=5)                    
                return

            db.close()

        except Exception, e:
            QApplication.restoreOverrideCursor()          
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
