# Makefile for a PyQGIS plugin 
UI_FILES =  base/help/Ui_about.py base/settings/Ui_options.py base/file/Ui_importproject.py

RESOURCE_FILES = resources.py



default: compile
	
compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<
