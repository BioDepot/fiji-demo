import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWpindel_config(OWBwBWidget):
    name = "pindel_config"
    description = "Generates pindel bam config file"
    priority = 72
    icon = getIconName(__file__,"pindel.png")
    want_main_area = False
    docker_image_name = "biodepot/pindel-gdc"
    docker_image_tag = "0.2.5b8__10f065ec"
    inputs = [("inputfiles",str,"handleInputsinputfiles"),("Trigger",str,"handleInputsTrigger"),("configuration",str,"handleInputsconfiguration")]
    outputs = [("configuration",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    inputfiles=pset([])
    configuration=pset([])
    filetags=pset([])
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"pindel_config")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsinputfiles(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputfiles", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsconfiguration(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("configuration", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"configuration"):
            outputValue=getattr(self,"configuration")
        self.send("configuration", outputValue)
