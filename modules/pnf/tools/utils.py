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
import collections

def fubar():
    print "foobar super"
    
def getCheckTopics(iface):
    filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/pnf/checks/checks.json"))
    
    if not filename:
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "checks.json not found."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return        
        
    try:
        checks = json.load(open(filename), object_pairs_hook=collections.OrderedDict) 
    except Exception, e:
        print "Couldn't do it: %s" % e        
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Failed to load checks.json."), level=QgsMessageBar.CRITICAL, duration=5)                            
        return

    try:
        topics = {}
        topic_names = []
        for check in checks["checks"]:
            topic = check["topic"]
            if topics.has_key(topic):
                continue
            topics[topic] = topic
            topic_names.append(topic)
        return topic_names
    except Exception, e:
        print "Couldn't do it: %s" % e        
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Error parsing json file."), level=QgsMessageBar.CRITICAL, duration=5)                            
        return
        
def getChecks(iface, topic):
    filename = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/pnf/checks/checks.json"))
    
    if not filename:
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "checks.json not found."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return        
        
    try:
        checks = json.load(open(filename), object_pairs_hook=collections.OrderedDict) 
    except Exception, e:
        print "Couldn't do it: %s" % e        
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Failed to load checks.json."), level=QgsMessageBar.CRITICAL, duration=5)                            
        return
    
    try:
        topic_checks = []
        for check in checks["checks"]:
            if topic == check["topic"]:
                topic_checks.append(check)
        return topic_checks
    except Exception, e:
        print "Couldn't do it: %s" % e        
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Error parsing json file."), level=QgsMessageBar.CRITICAL, duration=5)                            
        return

    
def loadLayer(iface, layer, collapsed_legend = False):
    settings = QSettings("CatAIS","Qcadastre")
    module_name = (settings.value("project/appmodule"))
    provider = (settings.value("project/provider"))
    dbhost = (settings.value("project/dbhost"))
    dbport = (settings.value("project/dbport"))
    dbname = (settings.value("project/dbname"))
    dbschema = (settings.value("project/dbschema"))
    dbuser = (settings.value("project/dbuser"))
    dbpwd = (settings.value("project/dbpwd"))
    dbadmin = (settings.value("project/dbadmin"))
    dbadminpwd = (settings.value("project/dbadminpwd"))
    
    if not dbhost or not dbport or not dbname or not dbschema or not dbuser or not dbpwd or not dbadmin or not dbadminpwd:
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Missing database parameter. Cannot load layer."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return
        
    if not module_name or not provider:
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Missing parameter. Cannot load layer."), level=QgsMessageBar.CRITICAL, duration=5)                    
        return

    try:
        if layer["type"] == "postgres":
            feature_type = str(layer["featuretype"])
            title = str(layer["title"])
            key = str(layer["key"])            
            
            try:
                geom = str(layer["geom"])
            except:
                geom = None
                
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
          
            # We can overwrite the active project settings/parameters to add *any* postgres layers.
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

            uri = QgsDataSourceURI()
            if layer["readonly"]:
                uri.setConnection(dbhost, dbport, dbname, dbuser, dbpwd)
            else:
                uri.setConnection(dbhost, dbport, dbname, dbadmin, dbadminpwd)
            uri.setDataSource(dbschema, feature_type, geom, sql, key)

#            print uri.uri()

            qgis_layer = QgsVectorLayer(uri.uri(), title, provider)
                        
            qml_path = QDir.convertSeparators(QDir.cleanPath(QgsApplication.qgisSettingsDirPath() + "/python/plugins/qcadastre/modules/"+module_name+"/qml/"+style))
            qml = QDir.convertSeparators(QDir.cleanPath(qml_path))
            qgis_layer.loadNamedStyle(qml)
    
            if not qgis_layer.isValid():
                iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Layer is not valid"), level=QgsMessageBar.CRITICAL, duration=5)                                                            
                return       
            else:
                QgsMapLayerRegistry.instance().addMapLayer(qgis_layer)

        elif layer["type"] == "wms":
            pass







        else:
            iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", "Data provider not supported: ") + str(layer["type"]), level=QgsMessageBar.CRITICAL, duration=5)                                                            
            return

        # Collapse legend in TOC.
        if collapsed_legend:
            legend_tree = iface.mainWindow().findChild(QDockWidget,"Legend").findChild(QTreeWidget)   
            legend_tree.collapseItem(legend_tree.currentItem())

        # Move layer into group.
        grp_list = iface.legendInterface().groups()
       
        try:
            grp_idx = grp_list.index(group)
        except ValueError:
            grp_idx = -1      

        if grp_idx >= 0:
            grp_idx_abs = getGroupIndex(iface, group)
            
            if grp_idx_abs <> 0:
                iface.legendInterface().moveLayer(qgis_layer, grp_idx)
                iface.legendInterface().setGroupExpanded(grp_idx-1,  False)
        else:      
            grp_idx = iface.legendInterface().addGroup(group)
            iface.legendInterface().moveLayer(qgis_layer, grp_idx)
   
        iface.legendInterface().setGroupExpanded(grp_idx,  False)





        return qgis_layer
        
    except Exception, e:
        print "Couldn't do it: %s" % e
        iface.messageBar().pushMessage("Error",  QCoreApplication.translate("QcadastreModule", unicode(e)), level=QgsMessageBar.CRITICAL, duration=5)                                                            
        return 
        

def getGroupIndex(iface, group_name):
    relation_list = iface.legendInterface().groupLayerRelationship()
    i = 0
    for item in relation_list:
        if item[0] == group_name:
            i = i  + 1
            return i
        i = i + 1
    return 0
