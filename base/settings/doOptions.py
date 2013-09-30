# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

from Ui_options import Ui_Options

class OptionsDialog(QDialog, Ui_Options):
  
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.bar = QgsMessageBar(self)
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding) 
        self.gridLayout.addWidget(self.bar, 0, 0, 1, 1, Qt.AlignTop)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)
        
        self.settings = QSettings("CatAIS","Qcadastre")
        self.projectsdatabase = self.settings.value("options/general/projectsdatabase")
        self.projectsdatabasepath = QFileInfo(self.projectsdatabase).absolutePath()
        self.projectsrootdir = self.settings.value("options/general/projectsrootdir")
        self.importjar = self.settings.value("options/import/jar")
        self.importjarpath = QFileInfo(self.importjar).absolutePath()
        self.providername = self.settings.value("options/db/provider")

    def initGui(self):        
        self.lineEditDbPort.setValidator(QRegExpValidator(QRegExp("[0-9]+"), self.lineEditDbPort))        
        
        self.lineEditProjectsDatabase.setText(self.settings.value("options/general/projectsdatabase")) 
        self.lineEditProjectsRootDir.setText(self.settings.value("options/general/projectsrootdir")) 
        
        self.lineEditImportJar.setText(self.settings.value("options/import/jar"))
        vmarguments = self.settings.value("options/import/vmarguments")
        if vmarguments == "":
            self.plainTextEditImportVMArguments.insertPlainText("-Xms128m -Xmx1024m")
        else:
            self.plainTextEditImportVMArguments.insertPlainText(vmarguments)
            
        self.cmbBoxDbProvider.addItem ("PostgreSQL", "postgres")
        self.cmbBoxDbProvider.addItem ("SQLite", "sqlite")
        idx = self.cmbBoxDbProvider.findData(self.providername)
        self.cmbBoxDbProvider.setCurrentIndex(idx)
        
        self.lineEditDbHost.setText(self.settings.value("options/db/host")) 
        self.lineEditDbDatabase.setText(self.settings.value("options/db/name")) 
        self.lineEditDbPort.setText(self.settings.value("options/db/port")) 
        self.lineEditDbUser.setText(self.settings.value("options/db/user")) 
        self.lineEditDbUserPwd.setText(self.settings.value("options/db/pwd"))  
        self.lineEditDbAdmin.setText(self.settings.value("options/db/admin")) 
        self.lineEditDbAdminPwd.setText(self.settings.value("options/db/adminpwd")) 

        QWidget.setTabOrder(self.cmbBoxDbProvider, self.lineEditDbHost)        
        QWidget.setTabOrder(self.lineEditDbHost, self.lineEditDbDatabase)
        QWidget.setTabOrder(self.lineEditDbDatabase, self.lineEditDbPort)
        QWidget.setTabOrder(self.lineEditDbPort, self.lineEditDbUser)
        QWidget.setTabOrder(self.lineEditDbUser, self.lineEditDbUserPwd)
        QWidget.setTabOrder(self.lineEditDbUserPwd, self.lineEditDbAdmin)
        QWidget.setTabOrder(self.lineEditDbAdmin, self.lineEditDbAdminPwd)

        self.listWidgetModelRepos.clear()
        size = self.settings.beginReadArray("options/modelrepositories")
        for i in range(size):
            self.settings.setArrayIndex(i)
            item = QListWidgetItem(self.settings.value("url"))
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.listWidgetModelRepos.addItem(item)
        self.settings.endArray();

    @pyqtSignature("on_btnAddModelRepo_clicked()")    
    def on_btnAddModelRepo_clicked(self):
        item = QListWidgetItem("http://")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.listWidgetModelRepos.addItem(item)
        self.listWidgetModelRepos.setFocus()
        self.listWidgetModelRepos.setCurrentRow(self.listWidgetModelRepos.count() - 1)

    @pyqtSignature("on_btnDeleteModelRepo_clicked()")    
    def on_btnDeleteModelRepo_clicked(self):
        selectedItems = self.listWidgetModelRepos.selectedItems()
        for selectedItem in self.listWidgetModelRepos.selectedItems():
            self.listWidgetModelRepos.takeItem(self.listWidgetModelRepos.row(selectedItem))

    @pyqtSignature("on_btnBrowseImportJar_clicked()")    
    def on_btnBrowseImportJar_clicked(self):
        file = QFileDialog.getOpenFileName(self, "Open import jar file", self.importjarpath, "jar (*.jar *.JAR)")
        fileInfo = QFileInfo(file)
        self.lineEditImportJar.setText(fileInfo.absoluteFilePath())

    @pyqtSignature("on_btnBrowseProjectsDatabase_clicked()")    
    def on_btnBrowseProjectsDatabase_clicked(self):
        file = QFileDialog.getOpenFileName(self, QCoreApplication.translate("Qcadastre", "Choose projects definitions database"), self.projectsdatabasepath,  "SQLite (*.sqlite *.db *.DB)")
        fileInfo = QFileInfo(file)
        self.lineEditProjectsDatabase.setText(fileInfo.absoluteFilePath())

    @pyqtSignature("on_btnBrowseProjectsRootDir_clicked()")    
    def on_btnBrowseProjectsRootDir_clicked(self):
        dir = QFileDialog.getExistingDirectory(self, QCoreApplication.translate("Qcadastre", "Choose projects root directory"), self.projectsrootdir)
        dirInfo = QFileInfo(dir)
        self.lineEditProjectsRootDir.setText(dirInfo.absoluteFilePath())
        
    @pyqtSignature("on_cmbBoxDbProvider_currentIndexChanged(int)")    
    def on_cmbBoxDbProvider_currentIndexChanged(self, idx):
        self.provider = self.cmbBoxDbProvider.itemData (idx)
        
        if self.provider == "postgres":
            self.lblDbHost.setEnabled(True)
            self.lineEditDbHost.setEnabled(True)
            self.lblDbDatabase.setEnabled(True)
            self.lineEditDbDatabase.setEnabled(True)
            self.lblDbPort.setEnabled(True)
            self.lineEditDbPort.setEnabled(True)
            self.lblDbUser.setEnabled(True)
            self.lineEditDbUser.setEnabled(True)
            self.lblDbUserPwd.setEnabled(True)
            self.lineEditDbUserPwd.setEnabled(True)
            self.lblDbAdmin.setEnabled(True)
            self.lineEditDbAdmin.setEnabled(True)
            self.lblDbAdminPwd.setEnabled(True)
            self.lineEditDbAdminPwd.setEnabled(True)
            
        elif self.provider == "sqlite":
            self.lblDbHost.setEnabled(False)
            self.lineEditDbHost.setEnabled(False)
            self.lblDbDatabase.setEnabled(False)
            self.lineEditDbDatabase.setEnabled(False)
            self.lblDbPort.setEnabled(False)
            self.lineEditDbPort.setEnabled(False)
            self.lblDbUser.setEnabled(False)
            self.lineEditDbUser.setEnabled(False)
            self.lblDbUserPwd.setEnabled(False)
            self.lineEditDbUserPwd.setEnabled(False)
            self.lblDbAdmin.setEnabled(False)
            self.lineEditDbAdmin.setEnabled(False)
            self.lblDbAdminPwd.setEnabled(False)
            self.lineEditDbAdminPwd.setEnabled(False)
            
            self.bar.pushMessage("Warning", "SQLite provider is not yet implemented.", level=QgsMessageBar.WARNING, duration=5)
            
    def accept(self):
        self.settings.setValue("options/general/projectsdatabase", self.lineEditProjectsDatabase.text())
        self.emit(SIGNAL("projectsFileHasChanged()"))
     
        self.settings.setValue("options/general/projectsrootdir", self.lineEditProjectsRootDir.text())

        self.settings.setValue("options/import/jar", self.lineEditImportJar.text())
        self.settings.setValue("options/import/vmarguments", self.plainTextEditImportVMArguments.toPlainText())

        self.settings.setValue("options/db/provider", self.provider)
        self.settings.setValue("options/db/host", self.lineEditDbHost.text())
        self.settings.setValue("options/db/name", self.lineEditDbDatabase.text())
        self.settings.setValue("options/db/port", self.lineEditDbPort.text())
        self.settings.setValue("options/db/user", self.lineEditDbUser.text())
        self.settings.setValue("options/db/pwd", self.lineEditDbUserPwd.text())
        self.settings.setValue("options/db/admin", self.lineEditDbAdmin.text())
        self.settings.setValue("options/db/adminpwd", self.lineEditDbAdminPwd.text())
      
        self.settings.beginWriteArray("options/modelrepositories");
        for i in range(self.listWidgetModelRepos.count()):
            self.settings.setArrayIndex(i);
            self.settings.setValue("url", self.listWidgetModelRepos.item(i).text());
        self.settings.endArray();        
        
        self.close()
