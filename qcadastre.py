# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qcadastre
                                 A QGIS plugin
 Rahmenfachschale
                              -------------------
        begin                : 2013-09-30
        copyright            : (C) 2013 by Stefan Ziegler
        email                : edi.gonzales@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources
import os.path


class Qcadastre:

    def __init__(self, iface):
        self.iface = iface
        self.mysettings = QSettings("CatAIS","Qcadastre")
        
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'qcadastre_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.action = QAction(
            QIcon(":/plugins/qcadastre/icon.png"),
            u"Qcadastre", self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Qcadastre", self.action)
        
        # main toolbar
        self.toolBar = self.iface.addToolBar("Qcadastre Main Toolbar")
        self.toolBar.setObjectName("QcadastreMainToolBar")
        self.toolBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))        
        
        # projects
        self.menuBarProjects = QMenuBar()
        self.menuBarProjects.setObjectName("Qcadastre.Main.ProjectsMenuBar")                
        self.menuBarProjects.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred))
        self.menuProjects = QMenu()
        self.menuProjects.setTitle(QCoreApplication.translate( "Qcadastre","Projects"))
        self.menuBarProjects.addMenu(self.menuProjects)

        # files
        self.menuBarFile= QMenuBar()
        self.menuBarFile.setObjectName("Qcadastre.Main.FileMenuBar")        
        self.menuBarFile.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.menuFile = QMenu()
        self.menuFile.setTitle(QCoreApplication.translate( "Qcadastre","File"))
        
        self.createproject = QAction(QCoreApplication.translate("Qcadastre", "Create empty project"), self.iface.mainWindow())
        #QObject.connect(self.createproject, SIGNAL("triggered()"), self.doCreateProject)        
        self.importproject = QAction(QCoreApplication.translate("Qcadastre", "Import project"), self.iface.mainWindow())
        QObject.connect(self.importproject, SIGNAL("triggered()"), self.doImportProject)
        self.deleteproject = QAction(QCoreApplication.translate("Qcadastre", "Delete project"), self.iface.mainWindow())     
        #QObject.connect(self.deleteproject, SIGNAL("triggered()"), self.doDeleteProject)             
        self.menuFile.addActions([self.createproject, self.importproject, self.deleteproject])
        self.menuBarFile.addMenu(self.menuFile) 
        
        # settings
        self.menuBarSettings = QMenuBar()
        self.menuBarSettings.setObjectName("Qcadastre.Main.SettingsMenuBar")
        self.menuBarSettings.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))        
        self.menuSettings = QMenu()
        self.menuSettings.setTitle(QCoreApplication.translate( "Qcadastre","Settings"))
        
        self.options = QAction(QCoreApplication.translate("QGeoApp", "Options"), self.iface.mainWindow())
        QObject.connect(self.options, SIGNAL("triggered()"), self.doOptions)     
        self.menuSettings.addActions([self.options])
        self.menuBarSettings.addMenu(self.menuSettings)        
        
        self.toolBar.addWidget(self.menuBarProjects) 
        self.toolBar.addWidget(self.menuBarFile)
        self.toolBar.addWidget(self.menuBarSettings)
        
    def doOptions(self):
        from base.settings.doOptions import OptionsDialog
        self.options_dlg = OptionsDialog(self.iface.mainWindow())
        self.options_dlg.initGui()
        self.options_dlg.show()
        #QObject.connect(self.opt_dlg, SIGNAL("projectsFileHasChanged()"), self.doLoadProjectsFile) 

    def doImportProject(self):
        from base.file.doImportProject import ImportProjectDialog
        self.import_dlg = ImportProjectDialog(self.iface.mainWindow())
        self.import_dlg.initGui()
        self.import_dlg.show()


    def unload(self):
        self.iface.removePluginMenu(u"&Qcadastre", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        pass
