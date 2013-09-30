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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Qcadastre"


def description():
    return "Rahmenfachschale"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Stefan Ziegler"

def email():
    return "edi.gonzales@gmail.com"

def classFactory(iface):
    # load Qcadastre class from file Qcadastre
    from qcadastre import Qcadastre
    return Qcadastre(iface)
