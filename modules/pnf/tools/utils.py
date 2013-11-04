# -*- coding:  utf-8 -*-
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import time
import os
import json
import locale
import sys

def fubar():
    print "foobar super"
    
def loadLayer(iface, layer, collapsed_legend = False):
    settings = QSettings("CatAIS","Qcadastre")
    module_name = str(settings.value("project/active/appmodule"))
    provider = str(settings.value("project/active/provider"))
    dbhost = str(settings.value("project/active/dbhost"))
    dbport = str(settings.value("project/active/dbport"))
    dbname = str(settings.value("project/active/dbname"))
    dbschema = str(settings.value("project/active/dbschema"))
    dbuser = str(settings.value("project/active/dbuser"))
    dbpwd = str(settings.value("project/active/dbpwd"))
    dbadmin = str(settings.value("project/active/dbadmin"))
    dbadminpwd = str(settings.value("project/active/dbadminpwd"))
    
    if dbhost == "" or dbport == "" or dbname == "" or dbschema == "" or dbuser == "" or dbpwd == ""  or dbadmin == "" or dbadminpwd == "":
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Missing database parameter. Cannot load layer."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return
        
    if module_name == "" or provider == "":
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Missing parameter. Cannot load layer."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return

    try:
        
        if layer["type"] == "postgres":
            feature_type = str(layer["featuretype"])
            title = unicode(layer["title"])
            key = str(layer["key"])            
            
            try:
                geom = str(layer["geom"])
            except:
                geom = ""
                
            try:
                style = str(layer["style"])
            except:
                style = ""
                
            try:
                group = unicode(layer["group"])
            except:
                group = None
                
            try:
                sql = str(layer["sql"])
            except:
                sql = ""
          
            # We can overwrite the active project settings/parameters to add any postgres layers.
            try:
                params = layer["params"]
                module_name = params["appmodule"]
                provider = params["provider"]
                dbhost = params["dbhost"]
                dbport = params["dbport"]
                dbname = params["dbname"]
                dbschema = params["dbschema"]
                dbuser = params["dbuser"]
                dbpwd = params["dbpwd"]
                dbadmin = params["dbadmin"]
                dbadminpwd = params["dbadminpwd"]
            except:
                pass


        
# qgis_layer?? qlayer???
        
        
    except Exception, e:
        print "Couldn't do it: %s" % e
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", unicode(e)), level=QgsMessageBar.CRITICAL, duration=5)                                                            
        return 
        
