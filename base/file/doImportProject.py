# -*- coding: utf-8 -*-

# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from qgis.gui import *
import os
import json
import sys
import tempfile
import time
import shutil
import codecs

from Ui_importproject import Ui_ImportProject

class ImportProjectDialog(QDialog, Ui_ImportProject):
  
    def __init__(self, parent, schemaOnly=False):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.schemaOnly = schemaOnly
        
        self.bar = QgsMessageBar(self)
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed) 
        self.gridLayout.addWidget(self.bar, 0, 0, 0, 1, Qt.AlignBottom)        
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setText("Import")
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","Qcadastre")
        self.inputitfpath = QFileInfo(self.settings.value("file/import/inputitfpath")).absolutePath()
        self.provider = self.settings.value("options/db/provider", "")
        if self.provider == "":
            self.provider = "postgres"

        today = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(today)
        self.dateTimeEdit.setCalendarPopup(True)


    def initGui(self):       
        self.lineEditDbSchema.setValidator(QRegExpValidator(QRegExp("[a-z0-9_]+"), self.lineEditDbSchema))
        
        if self.provider == "postgres":
            self.btnProjectName.setText("Check")
            self.lblProjectName.setText("Project name: ")
            self.lblProjectName.setEnabled(True)
            self.lineEditDbSchema.setEnabled(True)
            self.btnProjectName.setEnabled(True)            
        elif self.provider == "sqlite":
            self.lblProjectName.setText("Project file: ")            
            self.btnProjectName.setText("Browse")
            self.lblProjectName.setEnabled(False)
            self.lineEditDbSchema.setEnabled(False)
            self.btnProjectName.setEnabled(False)
 
        try:
            filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/modules.json"))
            self.modules = json.load(open(filename)) 
            if self.modules != None:
                sortedModulesList = sorted(self.modules["modules"], key=lambda k: k['displayname']) 
                self.cmbBoxAppModule.clear()
                for module in sortedModulesList:
                    self.cmbBoxAppModule.insertItem(self.cmbBoxAppModule.count(), unicode(module["displayname"]), [module["dirname"], module["ilimodel"], module["referenceframe"], module["epsg"]])
                self.cmbBoxAppModule.insertItem(0, QCoreApplication.translate("Qcadastre", "Choose module...."), None)
                self.cmbBoxAppModule.setCurrentIndex(0)
        except Exception, e:
            self.bar.pushMessage("Error", str(e), level=QgsMessageBar.CRITICAL)

    @pyqtSignature("on_btnProjectName_clicked()")    
    def on_btnProjectName_clicked(self):
        if self.provider == "postgres":
            self.bar.pushMessage("Warning", "This function is not yet implemented.", level=QgsMessageBar.WARNING, duration=5)
            pass
        elif self.provider == "sqlite":
            self.bar.pushMessage("Warning", "This function is not yet implemented.", level=QgsMessageBar.WARNING, duration=5)            
            # use "options/db/host" as setting parameter 
            pass

    @pyqtSignature("on_cmbBoxAppModule_currentIndexChanged(int)")      
    def on_cmbBoxAppModule_currentIndexChanged(self, idx):
        moduleData = self.cmbBoxAppModule.itemData(idx)
        
        if moduleData <> None:
            self.lineEditIliModelName.setText(moduleData[1])
            self.lineEditRefFrame.setText(moduleData[2] + " (EPSG:" + moduleData[3]  + ")")
            self.epsg = moduleData[3]
        else:
            self.lineEditIliModelName.clear()
            self.lineEditRefFrame.clear()
            self.epsg = ""

    @pyqtSignature("on_btnBrowsInputFile_clicked()")    
    def on_btnBrowsInputFile_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("Qcadastre", "Choose interlis transfer file"), self.inputitfpath,  "ITF (*.itf *.ITF)")
        fileInfo = QFileInfo(file)
        self.lineEditInputFile.setText(fileInfo.absoluteFilePath())


    def accept(self):
        # save the settings
        self.settings.setValue("file/import/inputitfpath", self.lineEditInputFile.text())
        self.settings.setValue("file/import/ili", self.lineEditIliModelName.text())

        # gather all data/information for properties file (needed by java import program)
        self.itf = self.lineEditInputFile.text()
        self.ili = self.lineEditIliModelName.text()
        self.dbschema = self.lineEditDbSchema.text()    
        moduleData = self.cmbBoxAppModule.itemData(self.cmbBoxAppModule.currentIndex())
        if moduleData <> None:
            self.appmodule = moduleData[0]
            self.appmodule_name = self.cmbBoxAppModule.currentText()
        else:
            self.appmodule = ""
            self.appmodule_name = ""
            
        self.datadate = self.dateTimeEdit.date().toString("yyyy-MM-dd")

        self.dbhost = self.settings.value("options/db/host")
        self.dbname = self.settings.value("options/db/name")
        self.dbport = self.settings.value("options/db/port")
        self.dbuser = self.settings.value("options/db/user")
        self.dbpwd = self.settings.value("options/db/pwd")
        self.dbadmin = self.settings.value("options/db/admin")
        self.dbadminpwd = self.settings.value("options/db/adminpwd")
        
        self.repositories = ""
        size = self.settings.beginReadArray("options/modelrepositories")
        for i in range(size):
            self.settings.setArrayIndex(i)
            self.repositories = self.repositories + "," + self.settings.value("url")
        self.settings.endArray();
        
        self.projectsdatabase = self.settings.value("options/general/projectsdatabase") 
        self.projectsrootdir = self.settings.value("options/general/projectsrootdir") 
        
        importjarpath = self.settings.value("options/import/jar") 
        importvmargs = self.settings.value("options/import/vmarguments") 
        
        # check if we have everything
        if self.itf == "" and self.schemaOnly == False:
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No Interlis Transfer File set."), level=QgsMessageBar.WARNING, duration=5)
            return
        
        if self.ili == "":
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No Interlis Model Name set."), level=QgsMessageBar.WARNING, duration=5)            
            return
            
        if self.dbschema == "":
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No database schema set."), level=QgsMessageBar.WARNING, duration=5)            
            return
            
        if self.cmbBoxAppModule.currentIndex() == 0:
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No application module chosen."), level=QgsMessageBar.WARNING, duration=5)            
            return
            
        if self.dbhost == None or self.dbname == None or self.dbport == None or self.dbuser == None or self.dbpwd == None or self.dbadmin == None or self.dbadminpwd == None:
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "Missing database parameters."), level=QgsMessageBar.WARNING, duration=5)                        
            return
        
#        Momentan noch hardcodiert im Importprogramm, darum bringt das hier noch nichts.
#        if self.repositories == "":
#            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No Interlis Model repository found."), level=QgsMessageBar.WARNING, duration=5)            
#            return
            
        if self.projectsrootdir == "":
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No root directory for projects set."), level=QgsMessageBar.WARNING, duration=5)                                    
            return
            
        if self.projectsdatabase == "":
            #self.bar.pushMessage("Information",  QCoreApplication.translate("Qcadastre", "No projects database found. Will create one in project root directory."), level=QgsMessageBar.INFO, duration=5)                        
            QMessageBox.warning(None, "Qcadastre", QCoreApplication.translate("Qcadastre", "No projects database found. Will create one in the project root directory."))
            
        if importjarpath == "":
            self.bar.pushMessage("Warning",  QCoreApplication.translate("Qcadastre", "No jar file set for import."), level=QgsMessageBar.WARNING, duration=5)                                                
            return
            
        # create java properties file
        tmpPropertiesFile = self.writePropertiesFile()
        if tmpPropertiesFile == None:
            return
            
        # clear output textedit
        self.textEditImportOutput.clear()
                
        # import data
        arguments = []
        
        vmargs = importvmargs.split(" ")
        for i in range(len(vmargs)):
            arguments.append(vmargs[i])
            
        arguments.append("-jar")
        arguments.append(importjarpath)
        arguments.append(tmpPropertiesFile)
        
        self.process = QProcess()
        self.connect(self.process, SIGNAL("readyReadStandardOutput()"), self.readOutput)
        self.connect(self.process, SIGNAL("readyReadStandardError()"), self.readError)
        self.connect(self.process, SIGNAL("finished(int)"), self.finishImport)     
     
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.buttonBox.setEnabled(False)
        try:
            self.process.start("java", arguments)
        except:
            QApplication.restoreOverrideCursor()
            self.buttonBox.setEnabled(True)            

    def readOutput(self):
        self.textEditImportOutput.insertPlainText(str(self.process.readAllStandardOutput()))
        self.textEditImportOutput.ensureCursorVisible()        

    def readError(self):
        self.textEditImportOutput.insertPlainText(str(self.process.readAllStandardError()))        
        #QgsMessageLog.logMessage(str(self.process.readAllStandardError()), "Qcadastre")

    def finishImport(self,  i):
        QApplication.restoreOverrideCursor()        
        self.buttonBox.setEnabled(True)

        updated = self.updateProjectsDatabase()
        if not updated:
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Import process not sucessfully finished. Could not update projects database."), level=QgsMessageBar.CRITICAL, duration=5)            
            return

        # check if there are some errors/fatals in the output
        # Prüfung erst hier, da es einfacher ist den misslungenen Import zu löschen, wenn
        # in der Projektedatenbank bereits ein Eintrag ist.
        output = unicode(self.textEditImportOutput.toPlainText())
        if output.find("FATAL") > 0 or output.find("ERROR") > 0 or output.strip() == "":
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Import process not sucessfully finished."), level=QgsMessageBar.CRITICAL, duration=5)                                                                       
            return            
            
        # create project directory in projects root dir
        proj_dir = self.createProjectDir()
        if proj_dir:
            self.bar.pushMessage("Information",  QCoreApplication.translate("Qcadastre", "Import process finished."), level=QgsMessageBar.INFO, duration=10)                                                                       
        else:
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Import process not sucessfully finished. Could not create project directory."), level=QgsMessageBar.CRITICAL, duration=5)                                                                       

    def createProjectDir(self):
        try:
            os.makedirs(os.path.join(str(self.projectsrootdir), str(self.dbschema)))
            return True
        except:
            return False

    def writePropertiesFile(self):
        tmpDir = tempfile.gettempdir()
        tmpPropertiesFile = os.path.join(tmpDir, str(time.time()) + ".properties")
    
        try:
            # "utf-8" macht momentan beim Java-Import Probleme! (Scheint aber mal funktioniert zu haben).
            # Mit "iso-8859-1" funktionierts. Im Output-Fenster erscheint aber immer noch Kauderwelsch.
            # Das Java-Properties-File muss angeblich immer iso-8859-1 sein....
            f = codecs.open(tmpPropertiesFile, "w", "iso-8859-1")
        
            try:
                f.write("dbhost = " + self.dbhost + "\n")
                f.write("dbname = " + self.dbname + "\n")
                f.write("dbschema = " + self.dbschema + "\n")
                f.write("dbport = " + self.dbport + "\n")
                f.write("dbuser = " + self.dbuser + "\n")
                f.write("dbpwd = " + self.dbpwd + "\n")
                f.write("dbadmin = " + self.dbadmin + "\n")
                f.write("dbadminpwd = " + self.dbadminpwd + "\n")
                f.write("\n")
                f.write("epsg = " + self.epsg + "\n")
                f.write("\n")
                f.write("vacuum = false\n")
                f.write("reindex = false\n")
                f.write("\n")
                f.write("importModelName = " + str(self.ili) + "\n")
                f.write("importItfFile = " + unicode(self.itf) + "\n")
                f.write("\n")
                f.write("schemaOnly = " + str(self.schemaOnly) + "\n")
                f.write("\n")
                f.write("enumerationText = true\n")
                f.write("renumberTid = true\n")
                f.write("\n");
                f.write("qgisFiles = false\n")
                f.write("\n");
                
                filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/"+self.appmodule+"/postprocessing/postprocessing.db"))                    
                f.write("postprocessingDatabase = " + str(filename))
                
            finally:
                f.close()
                return tmpPropertiesFile
        
        except IOError, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Cannot create: " + tmpPropertiesFile), level=QgsMessageBar.CRITICAL, duration=5)                                                
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Import process not completed."), level=QgsMessageBar.CRITICAL, duration=5)                                                           
            return None
        
        return  None

    def updateProjectsDatabase(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE", "Projectdatabase")

        try:
            # Create a new projects database if there is none (copy one from the templates).
            if self.projectsdatabase == "":
                srcdatabase = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/templates/template_projects.db"))
                self.projectsdatabase = QDir.convertSeparators(QDir.cleanPath(self.projectsrootdir + "/projects.db"))
                shutil.copyfile(srcdatabase, self.projectsdatabase)
                self.settings.setValue("options/general/projectsdatabase", self.projectsdatabase)

            self.db.setDatabaseName(self.projectsdatabase) 

            if not self.db.open():
                self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Could not open projects database."), level=QgsMessageBar.CRITICAL, duration=5)                                                                            
                QgsMessageLog.logMessage(str(self.db.lastError().driverText()), "Qcadastre")
                return  
             
            projectrootdir = QDir.convertSeparators(QDir.cleanPath(self.projectsrootdir + "/" + str(self.dbschema)))
        
            sql = "INSERT INTO projects (id, displayname, dbhost, dbname, dbport, dbschema, dbuser, dbpwd, dbadmin, dbadminpwd, provider, epsg, ilimodelname, appmodule, appmodulename, projectrootdir, projectdir, datadate) \
VALUES ('"+str(self.dbschema)+"', '"+str(self.dbschema)+"', '"+str(self.dbhost)+"', '"+str(self.dbname)+"', "+str(self.dbport)+", '"+str(self.dbschema)+"', '"+str(self.dbuser)+"', '"+str(self.dbpwd)+"', \
'"+str(self.dbadmin)+"', '"+str(self.dbadminpwd)+"', 'postgres'," + str(self.epsg) + " , '"+str(self.ili)+"', '"+str(self.appmodule)+"','"+unicode(self.appmodule_name)+"', '"+str(self.projectsrootdir)+"', '"+projectrootdir+"', '"+self.datadate+"');"

            query = self.db.exec_(sql)
            
            if query.isActive() == False:
                self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while updating projects database."), level=QgsMessageBar.CRITICAL, duration=5)                                                
                return 
            
            self.db.close()
            self.emit(SIGNAL("projectsDatabaseHasChanged()"))
            return True
        
        except Exception, e:
            print "Couldn't do it: %s" % e
            self.bar.pushMessage("Error",  QCoreApplication.translate("Qcadastre", "Error occured while updating projects database."), level=QgsMessageBar.CRITICAL, duration=5)                                                            
            return 
