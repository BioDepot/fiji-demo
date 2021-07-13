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

class OWFile(OWBwBWidget):
    name = "File"
    description = "Enter and output a file"
    priority = 10
    icon = getIconName(__file__,"fiji.png")
    want_main_area = False
    docker_image_name = "biodepot/fiji"
    docker_image_tag = "latest"
    inputs = [("fijidir",str,"handleInputsfijidir")]
    outputs = [("fijidir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    fijidir=pset(None)
    installfiji=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"File")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsfijidir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fijidir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"fijidir"):
            outputValue=getattr(self,"fijidir")
        self.send("fijidir", outputValue)
