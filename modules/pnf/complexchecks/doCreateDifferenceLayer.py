 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
from Ui_createdifferencelayer import Ui_CreateDifferenceLayer
import datetime
import qcadastre.modules.pnf.tools.utils as utils


class CreateDifferenceDialog(QDialog, Ui_CreateDifferenceLayer):

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.bar = QgsMessageBar(self)
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed) 
        self.gridLayout.addWidget(self.bar, 0, 0, 0, 1, Qt.AlignBottom)                
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Create")
        self.connect(self.okButton, SIGNAL("accepted()"), lambda foo="bar": self.accept(foo)) # it gets stranger from day to day...  
        
    def initGui(self):             
        self.settings = QSettings("CatAIS","Qcadastre")
        filename = self.settings.value("options/general/projectsdatabase")
        module_name = self.settings.value("project/appmodule")

        if filename == "" or filename == None:
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "No project database found.") + str(self.db.lastError().driverText()) , level=QgsMessageBar.CRITICAL)                                        
            return
            
        self.projects = []

        try:
            self.db = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
            self.db.setDatabaseName(filename) 

            if  self.db.open() == False:
                self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Could not open database.") + str(self.db.lastError().driverText()) , level=QgsMessageBar.CRITICAL)                            
                return 

            sql = "SELECT * FROM projects WHERE appmodule = '"+module_name+"';"

            query = self.db.exec_(sql)
            
            if not query.isActive():
                # does not work on qgis startup...                
                #self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while fetching projects informations.") , level=QgsMessageBar.CRITICAL, duration=5)                            
                return 

            record = query.record()
            while query.next():
                project = {}
                project["id"] = str(query.value(record.indexOf("id")))
                project["displayname"] = str(query.value(record.indexOf("displayname")))
                project["dbhost"] = str(query.value(record.indexOf("dbhost")))
                project["dbname"] = str(query.value(record.indexOf("dbname")))
                project["dbport"] = str(query.value(record.indexOf("dbport")))
                project["dbschema"] = str(query.value(record.indexOf("dbschema")))                
                project["dbuser"] = str(query.value(record.indexOf("dbuser")))
                project["dbpwd"] = str(query.value(record.indexOf("dbpwd")))
                project["dbadmin"] = str(query.value(record.indexOf("dbadmin")))
                project["dbadminpwd"] = str(query.value(record.indexOf("dbadminpwd")))
                project["provider"] = str(query.value(record.indexOf("provider")))
                project["epsg"] = str(query.value(record.indexOf("epsg")))
                project["ilimodelname"] = str(query.value(record.indexOf("ilimodelname")))
                project["appmodule"] = str(query.value(record.indexOf("appmodule")))
                project["appmodulename"] = unicode(query.value(record.indexOf("appmodulename")))
                project["projectrootdir"] = str(query.value(record.indexOf("projectrootdir")))
                project["projectdir"] = str(query.value(record.indexOf("projectdir")))
                project["datadate"] = str(query.value(record.indexOf("datadate")))
                project["importdate"] = str(query.value(record.indexOf("importdate")))                
                project["datadate"] = str(query.value(record.indexOf("datadate")))
                project["notes"] = unicode(query.value(record.indexOf("notes")))
                
                self.projects.append(project)

            self.db.close()

        except Exception, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Could not read projects database.") , level=QgsMessageBar.CRITICAL)                                        
            return 
            
        if self.projects:
            for project in self.projects:
                self.cmbBoxProjectBefore.insertItem(self.cmbBoxProjectBefore.count(), unicode(project["displayname"]), project)
                self.cmbBoxProjectAfter.insertItem(self.cmbBoxProjectAfter.count(), unicode(project["displayname"]), project)
                
            self.cmbBoxProjectBefore.insertItem(0, QCoreApplication.translate("QcadastreModule", "Choose project..."), None)
            self.cmbBoxProjectBefore.setCurrentIndex(0)
            self.cmbBoxProjectAfter.insertItem(0, QCoreApplication.translate("QcadastreModule", "Choose project..."), None)
            self.cmbBoxProjectAfter.setCurrentIndex(0)

    @pyqtSignature("on_cmbBoxProjectBefore_currentIndexChanged(int)")      
    def on_cmbBoxProjectBefore_currentIndexChanged(self, idx):
        self.lineEditDateBefore.clear()        
        project_data = self.cmbBoxProjectBefore.itemData(idx)
        
        if project_data:
            self.dbschema_before = project_data["dbschema"]
            datadate = datetime.datetime.strptime(project_data["datadate"], "%Y-%m-%d").date()
            
            self.lineEditDateBefore.setText(datadate.strftime("%d. %B %Y"))
            self.textEditBefore.insertPlainText(project_data["notes"])
            
    @pyqtSignature("on_cmbBoxProjectAfter_currentIndexChanged(int)")      
    def on_cmbBoxProjectAfter_currentIndexChanged(self, idx):
        self.lineEditDateAfter.clear()        
        project_data = self.cmbBoxProjectAfter.itemData(idx)
        
        if project_data:
            self.dbschema_after = project_data["dbschema"]            
            datadate = datetime.datetime.strptime(project_data["datadate"], "%Y-%m-%d").date()
            
            self.lineEditDateAfter.setText(datadate.strftime("%d. %B %Y"))
            self.textEditAfter.insertPlainText(project_data["notes"])            
            
    def accept(self):
        if self.cmbBoxProjectBefore.currentIndex() == 0 or self.cmbBoxProjectAfter.currentIndex() == 0:
            self.bar.pushMessage("Warning",  QCoreApplication.translate("QcadastreModule", "No project choosen.") , level=QgsMessageBar.WARNING)                                                    
            return
        
        dbschema = self.settings.value("project/dbschema")
        dbhost = self.settings.value("project/dbhost")
        dbname = self.settings.value("project/dbname")
        dbport = self.settings.value("project/dbport")
        dbschema = self.settings.value("project/dbschema")
        dbadmin = self.settings.value("project/dbadmin")
        dbadminpwd = self.settings.value("project/dbadminpwd")

        if not dbhost or not dbname or not dbport or not dbschema or not dbadmin or not dbadminpwd:
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Should not reach here.") , level=QgsMessageBar.CRITICAL)                            

        db = QSqlDatabase.addDatabase("QPSQL", "PostgreSQL")
        db.setHostName(dbhost)
        db.setDatabaseName(dbname)
        db.setUserName(dbadmin)
        db.setPassword(dbadminpwd)
        try:
            db.setPort(int(dbport))
        except ValueError, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Port is not a integer value.") , level=QgsMessageBar.CRITICAL)                                        
            return
        
        if not db.open():
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Could not open database: ") + str(db.lastError().driverText()), level=QgsMessageBar.CRITICAL)                                        
            return

        # delete existing data in the tables
        sql = "BEGIN;"
        sql += "DELETE FROM "+dbschema+".t_bb_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_bb_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_fl_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_fl_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_li_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_li_after_except_before;"
        sql += "DELETE FROM "+dbschema+".t_eo_pt_before_except_after;"
        sql += "DELETE FROM "+dbschema+".t_eo_pt_after_except_before;"
        sql += "COMMIT;"

        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)        
        try:
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.buttonBox.setEnabled(True)                                
                self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while deleting data.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
                return
        
            sql = """
            BEGIN;
            -- BODENBEDECKUNG BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_bb_before_except_after (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_after;


            -- BODENBEDECKUNG AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_bb_after_except_before (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".bodenbedeckung_boflaeche
              ) AS linestrings
            ) AS segments_after;
            
            
            -- EO FLAECHE BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_fl_before_except_after (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after;
            
            
            -- EO FLAECHE AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_fl_after_except_before (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after;


            -- EO LINIE BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_li_before_except_after (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_flaechenelement
              ) AS linestrings
            ) AS segments_after;
            
            
            -- EO LINIE AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_li_after_except_before (the_geom)
            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_after+""".einzelobjekte_linienelement
              ) AS linestrings
            ) AS segments_before

            EXCEPT 

            SELECT CASE WHEN ST_X(sp) < ST_X(ep) THEN (ST_SnapToGrid(ST_MakeLine(sp,ep), 0.0001))
                        ELSE (ST_SnapToGrid(ST_MakeLine(ep,sp), 0.0001))
                   END
            FROM
            (
              SELECT
                ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
                ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
              FROM
              (
                SELECT (ST_Dump(ST_Boundary(geometrie))).geom
                FROM """+self.dbschema_before+""".einzelobjekte_linienelement
              ) AS linestrings
            ) AS segments_after;

            -- EO PUNKT BEFORE EXCEPT AFTER
            INSERT INTO """+dbschema+""".t_eo_pt_before_except_after (the_geom)            
            SELECT geometrie
            FROM """+self.dbschema_before+""".einzelobjekte_punktelement

            EXCEPT

            SELECT geometrie
            FROM """+self.dbschema_after+""".einzelobjekte_punktelement;

            -- EO PUNKT AFTER EXCEPT BEFORE
            INSERT INTO """+dbschema+""".t_eo_pt_after_except_before (the_geom)            
            SELECT geometrie
            FROM """+self.dbschema_after+""".einzelobjekte_punktelement

            EXCEPT

            SELECT geometrie
            FROM """+self.dbschema_before+""".einzelobjekte_punktelement;
            COMMIT;
            """
                        
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.buttonBox.setEnabled(True)                
                self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while creating data.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
                return

            db.close()
            
        except Exception, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while deleting/creating data.") , level=QgsMessageBar.CRITICAL)                                                        
            QApplication.restoreOverrideCursor()        
            self.buttonBox.setEnabled(True)
            return
            
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)
        self.bar.pushMessage("Information",  QCoreApplication.translate("QcadastreModule", " Difference layer created.") , level=QgsMessageBar.INFO)                                                        



#        self.settings = QSettings("CatAIS","Qcadastre")
#        project_id = (self.settings.value("project/id"))
#        epsg = (self.settings.value("project/epsg"))
#        
#        if not project_id:
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "project_id not set"), level=QgsMessageBar.CRITICAL, duration=5)                                
#            return
#        
#        QApplication.setOverrideCursor(Qt.WaitCursor)
#        try:
#            group = "Lagekontrolle - Bahn" + " (" + str(project_id) + ")"
#            
#            layer = {}
#            layer["type"] = "wms"
#            layer["title"] = "Orthofoto CIR"
#            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
#            layer["layers"] = "Orthofoto11_CIR"
#            layer["format"] = "image/jpeg"
#            layer["crs"] = "EPSG:21781"
#            layer["group"] = group
#            
#            rlayer = utils.loadLayer(self.iface, layer)         
#            
#            layer = {}
#            layer["type"] = "wms"
#            layer["title"] = "Orthofoto RGB"
#            layer["url"] = "http://www.sogis1.so.ch/cgi-bin/sogis/sogis_orthofoto.wms"
#            layer["layers"] = "Orthofoto_SO"
#            layer["format"] = "image/jpeg"
#            layer["crs"] = "EPSG:21781"
#            layer["group"] = group
#            
#            rlayer = utils.loadLayer(self.iface, layer) 
#            if rlayer:
#                self.iface.legendInterface().setLayerVisible(rlayer, True)     
#                
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = "Gemeindegrenze"
#            layer["featuretype"] = "gemeindegrenzen_gemeindegrenze"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = "true"
#            layer["group"] = group
#            layer["style"] = "gemeindegrenze/gemgre_strichliert.qml"
#
#            gemgrelayer = utils.loadLayer(self.iface, layer) 
#            if gemgrelayer:
#                self.iface.legendInterface().setLayerVisible(gemgrelayer, True)     
#              
#    #        layer = {}
#    #        layer["type"] = "postgres"
#    #        layer["title"] = "SBB-Gleisnetz"
#    #        layer["featuretype"] = "gleisnetz"
#    #        layer["geom"] = "geom"
#    #        layer["key"] = "gid"            
#    #        layer["sql"] = ""
#    #        layer["readonly"] = True
#    #        layer["group"] = group
#    #        layer["style"] = "sbb/gleisnetz.qml"
#    #         
#    #        params =  {}
#    #        params["appmodule"] = str(self.settings.value("project/active/appmodule").toString())
#    #        params["subappmodule"] = str(self.settings.value("project/active/subappmodule").toString())      
#    #        params["provider"] = "postgres"
#    #        params["dbhost"] = str(self.settings.value("project/active/dbhost").toString())
#    #        params["dbport"] = str(self.settings.value("project/active/dbport").toString())
#    #        params["dbname"] = "pnf_varia"
#    #        params["dbschema"] = "sbb"
#    #        params["dbuser"] = str(self.settings.value("project/active/dbuser").toString())
#    #        params["dbpwd"] = str(self.settings.value("project/active/dbpwd").toString())
#    #        params["dbadmin"] = str(self.settings.value("project/active/dbadmin").toString())
#    #        params["dbadminpwd"] = str(self.settings.value("project/active/dbadminpwd").toString())
#    #        
#    #        layer["params"] = params
#    #
#    #        vlayer = self.qutils.loadProjectLayer(self.iface, layer)    
#    #        if vlayer <> False:
#    #            self.iface.legendInterface().setLayerVisible(vlayer, True)    
#
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = "BB.BoFlaeche"
#            layer["featuretype"] = "bodenbedeckung_boflaeche"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = True
#            layer["group"] = group
#            layer["style"] = "bb/bb_bahn_ortho.qml"
#
#            vlayer = utils.loadLayer(self.iface, layer)    
#            if vlayer:
#                self.iface.legendInterface().setLayerVisible(vlayer, True)    
#
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = u"EO.Flaechenelement"
#            layer["featuretype"] = "v_einzelobjekte_flaechenelement"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = True
#            layer["group"] = group
#            layer["style"] = "eo/eo_fl_bahn_ortho.qml"
#
#            vlayer = utils.loadLayer(self.iface, layer)    
#            if vlayer:
#                self.iface.legendInterface().setLayerVisible(vlayer, True)    
#
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = u"EO.Linienelement"
#            layer["featuretype"] = "v_einzelobjekte_linienelement"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = True
#            layer["group"] = group
#            layer["style"] = "eo/eo_li_bahn_ortho.qml"
#
#            vlayer = utils.loadLayer(self.iface, layer)    
#            if vlayer:
#                self.iface.legendInterface().setLayerVisible(vlayer, True)    
#
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = u"EO.Punktelement"
#            layer["featuretype"] = "v_einzelobjekte_punktelement"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = True
#            layer["group"] = group
#            layer["style"] = "eo/eo_pk_andere.qml"
#
#            vlayer = utils.loadLayer(self.iface, layer)    
#            if vlayer:
#                self.iface.legendInterface().setLayerVisible(vlayer, True)    
#
#            layer = {}
#            layer["type"] = "postgres"
#            layer["title"] = u"LI.Liegenschaft"
#            layer["featuretype"] = "liegenschaften_liegenschaft"
#            layer["geom"] = "geometrie"
#            layer["key"] = "ogc_fid"            
#            layer["sql"] = ""
#            layer["readonly"] = True
#            layer["group"] = group
#            layer["style"] = "li/liegenschaft_ortho.qml"
#
#            vlayer = utils.loadLayer(self.iface, layer)    
#            if vlayer:
#                self.iface.legendInterface().setLayerVisible(vlayer, False)    
#
#            if gemgrelayer <> False:
#                rect = gemgrelayer.extent()
#                rect.scale(1.2)
#                self.iface.mapCanvas().setExtent(rect)        
#                self.iface.mapCanvas().refresh() 
#
#        except Exception, e:
#            QApplication.restoreOverrideCursor()            
#            print "Couldn't do it: %s" % e            
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
#        QApplication.restoreOverrideCursor()        
#
#        # Workaround for geometryless-tables-wgs84-bug.
#        try:
#            self.canvas.setMapUnits(0)		
#            srs = QgsCoordinateReferenceSystem()
#            srs.createFromSrid(int(epsg))
#            renderer = self.canvas.mapRenderer()
#            renderer.setDestinationCrs(srs)
#        except Exception, e:
#            print "Couldn't do it: %s" % e            
#            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                    
