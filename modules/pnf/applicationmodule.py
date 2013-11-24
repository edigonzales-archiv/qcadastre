 # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os
import json
import time
import sys

import tools.utils as utils


class ApplicationModule(QObject):
    
    def __init__(self, iface, toolBar):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.toolBar = toolBar
        
        self.settings = QSettings("CatAIS","Qcadastre")
        
    def initGui(self):
        self.cleanGui()
        self.doInitChecksMenu()
        self.doInitDefectsMenu()
        
        verification = os.getenv('QGIS_PNF_VERIFIKATION', 0)
        
        if verification:
            self.doInitVerificationMenu()
        
    def doInitVerificationMenu(self):    
        menuBar = QMenuBar(self.toolBar)
        menuBar.setObjectName("QcadastreModule.LoadVerificationMenuBar")        
        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        menu = QMenu(menuBar)
        menu.setTitle(QCoreApplication.translate( "QcadastreModule","Verification"))  
        
        topics = utils.getVerificationTopics(self.iface)
        if topics:
            for topic in topics:
                verificationfile = topic["file"]
                mytopic = topic["topic"]
                singleVerificationMenu = menu.addMenu(unicode(mytopic))    
                verifications = utils.getVerifications(self.iface, verificationfile)

                for verification in verifications:
                    verification_name = unicode(verification["name"])
                    action = QAction(verification_name, self.iface.mainWindow())
                    singleVerificationMenu.addAction(action)                                         
                    QObject.connect(action, SIGNAL( "triggered()"), lambda complexCheck=verification: self.doShowComplexCheck(complexCheck))

        menuBar.addMenu(menu)
        self.toolBar.insertWidget(self.beforeAction, menuBar)

    def doInitChecksMenu(self):
        menuBar = QMenuBar(self.toolBar)
        menuBar.setObjectName("QcadastreModule.LoadChecksMenuBar")        
        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        menu = QMenu(menuBar)
        menu.setTitle(QCoreApplication.translate( "QcadastreModule","Checks"))  
        
        topics = utils.getCheckTopics(self.iface)
        if topics:
            for topic in topics:
                checkfile = topics[topic]['file']
                singleCheckMenu = menu.addMenu(unicode(topic))                        
                checks = utils.getChecks(self.iface, checkfile)
                
                for check in checks:
                    checkName = unicode(check["name"])
                    if checkName == "separator":
                        singleCheckMenu.addSeparator()
                    else:
                        action = QAction(checkName, self.iface.mainWindow())
                        singleCheckMenu.addAction(action)                                         
                        QObject.connect(action, SIGNAL( "triggered()"), lambda complexCheck=check: self.doShowComplexCheck(complexCheck))

        menuBar.addMenu(menu)
        self.toolBar.insertWidget(self.beforeAction, menuBar)

    def doShowComplexCheck(self, check):
        try:
            module = str(check["file"])
            print module
            _temp = __import__(module, globals(), locals(), ['ComplexCheck'])
            c = _temp.ComplexCheck(self.iface)
            c.run()
        except Exception, e:
            print "Couldn't do it: %s" % e
            self.iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", str(e)), level=QgsMessageBar.CRITICAL, duration=5)                                


    def doInitDefectsMenu(self):
        menuBar = QMenuBar(self.toolBar)
        menuBar.setObjectName("QcadastreModule.LoadDefectsMenuBar")        
        menuBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        menu = QMenu(menuBar)
        menu.setTitle(QCoreApplication.translate( "QcadastreModule","Defects"))  

        action = QAction(QCoreApplication.translate("QcadastreModule", "Load defects layer"), self.iface.mainWindow())
        QObject.connect(action, SIGNAL( "triggered()"), lambda foo="bar": self.doLoadDefects(foo))
        menu.addAction(action)     
        
        action = QAction(QCoreApplication.translate("QcadastreModule", "Export defects layer"), self.iface.mainWindow())
        QObject.connect(action, SIGNAL( "triggered()"), lambda foo="bar": self.doExportDefects(foo))
        menu.addAction(action)     

        menuBar.addMenu(menu)
        self.toolBar.insertWidget(self.beforeAction, menuBar)

    def doLoadDefects(self, bar):
        from tools.doLoadDefects import LoadDefects
        d = LoadDefects(self.iface)
        d.run()


    def doExportDefects(self, foo):
        from tools.doExportDefects import ExportDefects        
        d = ExportDefects(self.iface)
        d.run()

    def cleanGui(self):
        # remove all the applications module specific menus
        actions = self.toolBar.actions()
        for action in actions:
            try:
                objectName = action.defaultWidget().objectName()
                # delete existing module menus
                if objectName[0:15] == "QcadastreModule":
                    self.toolBar.removeAction(action)
                # remember the action where we want to insert our new menu 
                # (e.g. settings menu bar)
                if objectName == "Qcadastre.Main.SettingsMenuBar":
                    self.beforeAction = action
                # get settings menu bar for module specific settings
                if objectName == "Qcadastre.Main.SettingsMenuBar":
                    self.settingsAction = action
            except AttributeError:
                pass
                
        # remove all the application module specific options/settings in the settings menu
        settingsMenuBar = self.settingsAction.defaultWidget()
        settingsMenu = self.settingsAction.defaultWidget().actions()[0].parentWidget()
        
        actions = settingsMenu.actions()
        for action in actions:
            objectName = action.objectName()
            if objectName[0:15] == "QcadastreModule":
               settingsMenu.removeAction(action) 
            
            if action.isSeparator():
                settingsMenu.removeAction(action)

    def run(self):
        print "fubar"

        
        


