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

class OWdownloadURL(OWBwBWidget):
    name = "downloadURL"
    description = "Downloads files from URL"
    priority = 10
    icon = getIconName(__file__,"download.png")
    want_main_area = False
    docker_image_name = "biodepot/downloadurl"
    docker_image_tag = "alpine_3.13.2__b2680386"
    inputs = [("downloadDir",str,"handleInputsdownloadDir"),("trigger",str,"handleInputstrigger")]
    outputs = [("downloadDir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    URL=pset([])
    decompress=pset(True)
    downloadDir=pset(None)
    concatenateFile=pset(None)
    noClobber=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"downloadURL")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsdownloadDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("downloadDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue="/data"
        if hasattr(self,"downloadDir"):
            outputValue=getattr(self,"downloadDir")
        self.send("downloadDir", outputValue)
