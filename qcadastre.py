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

    def __init__(self, iface, version):
        self.iface = iface
        self.version = version
        self.settings = QSettings("CatAIS","Qcadastre")
        
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
        QObject.connect(self.deleteproject, SIGNAL("triggered()"), self.doDeleteProject)             
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
        
        # help
        self.menuBarHelp = QMenuBar()
        self.menuBarHelp.setObjectName("Qcadastre.Main.HelpMenuBar")
        self.menuBarHelp.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))                
        self.menuHelp = QMenu()
        self.menuHelp.setTitle(QCoreApplication.translate("Qcadastre","Help"))
        
        self.about = QAction(QCoreApplication.translate("QGeoApp", "About"), self.iface.mainWindow())
        QObject.connect(self.about, SIGNAL("triggered()"), self.doAbout)        
        
        self.menuHelp.addActions([self.about])
        self.menuBarHelp.addMenu(self.menuHelp)

        # add menus to toolbar
        self.toolBar.addWidget(self.menuBarProjects) 
        self.toolBar.addWidget(self.menuBarFile)
        self.toolBar.addWidget(self.menuBarSettings)
        self.toolBar.addWidget(self.menuBarHelp)
        
        # initial load of project menu entries
        self.doLoadProjectsDatabase()        

    def doAbout(self):
        from base.help.doAbout import AboutDialog
        self.about_dlg = AboutDialog(self.iface.mainWindow(), self.version)
        self.about_dlg.show()

    def doOptions(self):
        from base.settings.doOptions import OptionsDialog
        self.options_dlg = OptionsDialog(self.iface.mainWindow())
        self.options_dlg.initGui()
        self.options_dlg.show()
        QObject.connect(self.options_dlg, SIGNAL("projectsDatabaseHasChanged()"), self.doLoadProjectsDatabase) 

    def doImportProject(self):
        from base.file.doImportProject import ImportProjectDialog
        self.import_dlg = ImportProjectDialog(self.iface.mainWindow())
        self.import_dlg.initGui()
        self.import_dlg.show()
        QObject.connect(self.import_dlg, SIGNAL("projectsDatabaseHasChanged()"), self.doLoadProjectsDatabase)         
        
    def doDeleteProject(self):
        from base.file.doDeleteProject import DeleteProjectDialog
        self.delete_dlg = DeleteProjectDialog(self.iface.mainWindow())
        self.delete_dlg.initGui()
        self.delete_dlg.show()
        QObject.connect(self.delete_dlg, SIGNAL("projectsDatabaseHasChanged()"), self.doLoadProjectsDatabase) 

    def doLoadProjectsDatabase(self):
        from base.projects.doLoadProjectsDatabase import LoadProjectsDatabase
        d = LoadProjectsDatabase(self.iface.messageBar())
        projects = d.read()
        
        if projects != None:
            groupedProjects = {}
            for project in projects:
                moduleName = project["appmodulename"]
                try:
                    moduleList = groupedProjects[moduleName]
                except KeyError:
                    moduleList = []
                
                moduleList.append(project)
                groupedProjects[moduleName] = moduleList
            
            self.menuProjects.clear()
            for key in groupedProjects:
                modules = groupedProjects[key]
                groupMenu = self.menuProjects.addMenu(QCoreApplication.translate("Qcadastre", unicode(key)))
                sortedProjectsList = sorted(modules, key=lambda k: k['displayname']) 
                for project in sortedProjectsList:
                    action = QAction(QCoreApplication.translate("QGeoApp", unicode(project["displayname"])), self.iface.mainWindow())
                    groupMenu.addAction(action)
                    QObject.connect(action, SIGNAL( "triggered()"), lambda activeProject=project: self.doLoadProject(activeProject))

    def doLoadProject(self, project):
        self.settings.setValue("project/id", str(project["id"]))
        self.settings.setValue("project/displayname", str(project["displayname"]))
        self.settings.setValue("project/appmodule", str(project["appmodule"]))
        self.settings.setValue("project/appmodulename", unicode(project["appmodulename"]))
        self.settings.setValue("project/ilimodelname", str(project["ilimodelname"]))
        self.settings.setValue("project/epsg", str(project["epsg"]))
        self.settings.setValue("project/provider", str(project["provider"]))
        self.settings.setValue("project/dbhost", str(project["dbhost"]))
        self.settings.setValue("project/dbport", str(project["dbport"]))
        self.settings.setValue("project/dbname", str(project["dbname"]))
        self.settings.setValue("project/dbschema", str(project["dbschema"]))
        self.settings.setValue("project/dbuser", str(project["dbuser"]))
        self.settings.setValue("project/dbpwd", str(project["dbpwd"]))
        self.settings.setValue("project/dbadmin", str(project["dbadmin"]))
        self.settings.setValue("project/dbadminpwd", str(project["dbadminpwd"]))
        self.settings.setValue("project/projectdir", str(project["projectdir"]))
        
        moduleName = str(project["appmodule"]).lower()

        try:
            _temp = __import__("modules." + moduleName + ".applicationmodule", globals(), locals(), ['ApplicationModule'])
            c = _temp.ApplicationModule(self.iface, self.toolBar)
            c.initGui()
#            c.run()            
        except Exception, e:
            print "Couldn't do it: %s" % e            
            QMessageBox.critical(None, "Qcadastre",  QCoreApplication.translate("QGeoApp", "Module '" + moduleName + "' import error."))


    def unload(self):
        self.iface.removePluginMenu(u"&Qcadastre", self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.mainWindow().removeToolBar(self.toolBar)

    def run(self):
        pass
