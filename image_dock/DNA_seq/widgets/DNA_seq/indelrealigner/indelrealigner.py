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

class OWindelrealigner(OWBwBWidget):
    name = "indelrealigner"
    description = "Indel realignment using GATK"
    priority = 40
    icon = getIconName(__file__,"gatk-realign.png")
    want_main_area = False
    docker_image_name = "biodepot/gatk3-co-clean"
    docker_image_tag = "3.6__804cb988"
    inputs = [("bamfiles",str,"handleInputsbamfiles"),("intervals",str,"handleInputsintervals"),("reference",str,"handleInputsreference"),("reference_trigger",str,"handleInputsreference_trigger"),("indels_trigger",str,"handleInputsindels_trigger"),("outputfiles",str,"handleInputsoutputfiles")]
    outputs = [("outputfiles",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    reference=pset(None)
    known=pset(None)
    bamfiles=pset([])
    intervals=pset([])
    outputfiles=pset([])
    nooriginaltags=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"indelrealigner")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsbamfiles(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamfiles", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsintervals(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("intervals", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference_trigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference_trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsindels_trigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("indels_trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputfiles(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputfiles", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputfiles"):
            outputValue=getattr(self,"outputfiles")
        self.send("outputfiles", outputValue)
