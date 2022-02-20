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

class OWmuse_sump(OWBwBWidget):
    name = "muse_sump"
    description = "MuSE variant caller"
    priority = 60
    icon = getIconName(__file__,"muse.png")
    want_main_area = False
    docker_image_name = "biodepot/muse"
    docker_image_tag = "1.0rc__alpine_3.13.2__104430b8"
    inputs = [("calloutput",str,"handleInputscalloutput"),("trigger",str,"handleInputstrigger"),("outputfile",str,"handleInputsoutputfile")]
    outputs = [("outputfile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    dbsnp=pset(None)
    exome=pset(False)
    genome=pset(False)
    outputfile=pset([])
    calloutput=pset([])
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"muse_sump")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputscalloutput(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("calloutput", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputfile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputfile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputfile"):
            outputValue=getattr(self,"outputfile")
        self.send("outputfile", outputValue)
