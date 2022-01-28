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

class OWmacro(OWBwBWidget):
    name = "macro"
    description = "Create FIJI BigStitcher Macro"
    priority = 10
    icon = getIconName(__file__,"script.png")
    want_main_area = False
    docker_image_name = "biodepot/alpine-bash"
    docker_image_tag = "3.7"
    inputs = [("trigger",str,"handleInputstrigger"),("pattern0",str,"handleInputspattern0"),("pattern1",str,"handleInputspattern1"),("inputPath",str,"handleInputsinputPath"),("savePath",str,"handleInputssavePath"),("timepointsPerPartition",str,"handleInputstimepointsPerPartition")]
    outputs = [("macroFile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    pattern0=pset("Channels")
    pattern1=pset("Tiles")
    inputPath=pset("/data/bigstitcher-data/Grid1")
    savePath=pset("/data/bigstitcher-data")
    timepointsPerPartition=pset("1")
    macroFile=pset("/data/bigstitcher-data/bigstitcher-macro.ijm")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"macro")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputspattern0(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("pattern0", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputspattern1(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("pattern1", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsinputPath(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputPath", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssavePath(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("savePath", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstimepointsPerPartition(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("timepointsPerPartition", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"macroFile"):
            outputValue=getattr(self,"macroFile")
        self.send("macroFile", outputValue)
