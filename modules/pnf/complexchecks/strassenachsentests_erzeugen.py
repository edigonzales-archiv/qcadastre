 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *

import qcadastre.modules.pnf.tools.utils as utils


class ComplexCheck(QObject):

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.settings = QSettings("CatAIS","Qcadastre")
        
        print "foo"

    def run(self):     
        print "asdf"
        dbschema = self.settings.value("project/dbschema")
        dbhost = self.settings.value("project/dbhost")
        dbname = self.settings.value("project/dbname")
        dbport = self.settings.value("project/dbport")
        dbschema = self.settings.value("project/dbschema")
        dbadmin = self.settings.value("project/dbadmin")
        dbadminpwd = self.settings.value("project/dbadminpwd")

        if not dbhost or not dbname or not dbport or not dbschema or not dbadmin or not dbadminpwd:
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Should not reach here.") , level=QgsMessageBar.CRITICAL)                            

        db = QSqlDatabase.addDatabase("QPSQL", "PostgreSQL")
        db.setHostName(dbhost)
        db.setDatabaseName(dbname)
        db.setUserName(dbadmin)
        db.setPassword(dbadminpwd)
        try:
            db.setPort(int(dbport))
        except ValueError, e:
            print "Couldn't do it: %s" % e
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Port is not a integer value.") , level=QgsMessageBar.CRITICAL)                                        
            return
        
        if not db.open():
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Could not open database: ") + str(db.lastError().driverText()), level=QgsMessageBar.CRITICAL)                                        
            return

        sql = "BEGIN;"
        sql += "DELETE FROM "+dbschema+".t_achsen_ausserhalb;"
        sql += "COMMIT;"
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while deleting data.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
                return

            sql = """
            BEGIN;            
            INSERT INTO """+dbschema+""".t_achsen_ausserhalb (the_geom)
            SELECT geom
            FROM
            (
             SELECT (ST_DumpPoints(geometrie)).geom
             FROM """+dbschema+""".gebaeudeadressen_strassenstueck
            ) as achse LEFT JOIN
            (
             SELECT ogc_fid, geometrie
             FROM """+dbschema+""".bodenbedeckung_boflaeche
             WHERE art = 1
            ) as str ON ST_Intersects(str.geometrie, achse.geom)
            WHERE str.ogc_fid IS NULL;
            COMMIT;
            """
                        
            query = db.exec_(sql)

            if not query.isActive():
                QApplication.restoreOverrideCursor()        
                self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while creating data.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
                return

            db.close()
            
        except Exception, e:
            print "Couldn't do it: %s" % e
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Something went wrong while deleting/creating data.") , level=QgsMessageBar.CRITICAL)                                                        
            QApplication.restoreOverrideCursor()        
            return
            
        QApplication.restoreOverrideCursor()        
        self.iface.messageBar().pushMessage("Information",  QCoreApplication.translate("QcadastreModule", "Layers created.") , level=QgsMessageBar.INFO)                                                        
