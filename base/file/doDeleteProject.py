# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
import os, json, sys, tempfile, time

from Ui_deleteproject import Ui_DeleteProject
from qcadastre.base.projects.doLoadProjectsDatabase import LoadProjectsDatabase

class DeleteProjectDialog(QDialog, Ui_DeleteProject):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.bar = QgsMessageBar(self)
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed) 
        self.gridLayout.addWidget(self.bar, 0, 0, 0, 1, Qt.AlignTop)        

        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Delete")
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","Qcadastre")
        self.projectsdatabase = self.settings.value("options/general/projectsdatabase") 

    def initGui(self):     
        d = LoadProjectsDatabase(self.bar)
        projects = d.read()
 
        if not projects:
            self.cBoxProject.clear()    
            return
        
        self.projects = projects
        sortedProjects = sorted(self.projects, key=lambda k: k['displayname']) 
    
        self.cBoxProject.clear()    
        for project in sortedProjects:
            self.cBoxProject.addItem(unicode(project["displayname"]), project["dbschema"])

        self.cBoxProject.insertItem(0, QCoreApplication.translate("Qcadastre", "Choose project...."), None)
        self.cBoxProject.setCurrentIndex(0)

    def accept(self):
        currIdx = self.cBoxProject.currentIndex()
        if currIdx == 0:
            return
        
        dbschema = str(self.cBoxProject.itemData(currIdx))
        
        i = 0
        for project in self.projects:
            if dbschema ==  str(project["dbschema"]):                
                self.dbhost = str(project["dbhost"])
                self.dbname = str(project["dbname"])
                self.dbport = str(project["dbport"])
                self.dbschema = dbschema
                self.dbadmin = str(project["dbadmin"])
                self.dbadminpwd = str(project["dbadminpwd"])
                self.projectIndex = i
            i += 1
                 
        if self.dbhost == None or self.dbname == None or self.dbport == None or self.dbschema == None or self.dbadmin == None or self.dbadminpwd == None:
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Should not reach here.") , level=QgsMessageBar.CRITICAL, duration=5)                            
            
        # delete geodata in db 
        db = QSqlDatabase.addDatabase("QPSQL", "PostgreSQL")
        db.setHostName(self.dbhost)
        db.setDatabaseName(self.dbname)
        db.setUserName(self.dbadmin)
        db.setPassword(self.dbadminpwd)
        try:
            db.setPort(int(self.dbport))
        except ValueError, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Port is not a integer value.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
            return
        
        if not db.open():
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Could not open database: ") + str(db.lastError().driverText()), level=QgsMessageBar.CRITICAL, duration=5)                                        
            return
            
        sql = "BEGIN;"
        sql += "DROP SCHEMA IF EXISTS " + self.dbschema + " CASCADE;"
        #sql += "DELETE FROM public.geometry_columns WHERE f_table_schema = '" + self.dbschema + "';"
        sql += "COMMIT;"
        
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)        
        try:
            query = db.exec_(sql)
            
            if query.isActive() == False:
                self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while deleting project.") , level=QgsMessageBar.CRITICAL, duration=5)                                        
                return
            
            db.close()
                
            # delete project entry in project database
            pdb = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")
            pdb.setDatabaseName(self.projectsdatabase) 

            if not pdb.open():
                self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Could not open projects database: ") + str(pdb.lastError().driverText()), level=QgsMessageBar.CRITICAL, duration=5)                                                        
                return 
                
            sql = "DELETE FROM projects WHERE dbschema = '" + self.dbschema + "';"

            query = pdb.exec_(sql)
            
            if not query.isActive():
                self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while updating projects database.") , level=QgsMessageBar.CRITICAL, duration=5)                                                        
                return 
            
            pdb.close()
            self.emit(SIGNAL("projectsDatabaseHasChanged()"))
            self.initGui()
            
        except Exception, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Something went wrong while deleting project.") , level=QgsMessageBar.CRITICAL, duration=5)                                                        
            QApplication.restoreOverrideCursor()        
            self.buttonBox.setEnabled(True)
            
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)
        self.bar.pushMessage("Information",  QCoreApplication.translate("Qcadastre", "Project deleted. Please remove project directory manually.") , level=QgsMessageBar.INFO, duration=5)                                                        

