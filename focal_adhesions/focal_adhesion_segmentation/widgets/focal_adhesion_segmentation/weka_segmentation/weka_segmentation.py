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

class OWweka_segmentation(OWBwBWidget):
    name = "weka_segmentation"
    description = "Run Trainable Weka Segmentation on an image."
    priority = 10
    icon = getIconName(__file__,"fiji.png")
    want_main_area = False
    docker_image_name = "biodepot/fiji_segmentation"
    docker_image_tag = "latest"
    inputs = [("fijidir",str,"handleInputsfijidir"),("installfiji",str,"handleInputsinstallfiji"),("trigger",str,"handleInputstrigger"),("imagefile",str,"handleInputsimagefile"),("classifier",str,"handleInputsclassifier")]
    outputs = [("outputfile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    fijidir=pset(None)
    installfiji=pset(None)
    overwrite=pset(False)
    imagefile=pset(None)
    classifier=pset(None)
    outputfile=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"weka_segmentation")) as f:
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
    def handleInputsinstallfiji(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("installfiji", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsimagefile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("imagefile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsclassifier(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("classifier", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputfile"):
            outputValue=getattr(self,"outputfile")
        self.send("outputfile", outputValue)
