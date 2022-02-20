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

class OWMuTect2(OWBwBWidget):
    name = "MuTect2"
    description = "MuTect2 variant caller"
    priority = 80
    icon = getIconName(__file__,"mutect2.png")
    want_main_area = False
    docker_image_name = "broadinstitute/gatk3"
    docker_image_tag = "3.6-0"
    inputs = [("bamtrigger",str,"handleInputsbamtrigger"),("ponstrigger",str,"handleInputsponstrigger"),("referenceFile",str,"handleInputsreferenceFile"),("inputNormalFile",str,"handleInputsinputNormalFile"),("inputTumorFile",str,"handleInputsinputTumorFile"),("outputFile",str,"handleInputsoutputFile"),("nct",str,"handleInputsnct"),("veptrigger",str,"handleInputsveptrigger"),("snpstrigger",str,"handleInputssnpstrigger")]
    outputs = [("outputFile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    inputNormalFile=pset([])
    inputTumorFile=pset([])
    referenceFile=pset(None)
    outputFile=pset([])
    intervals=pset(None)
    normalPanel=pset([])
    cosmic=pset([])
    dbsnp=pset(None)
    contamination=pset(None)
    outputMode=pset(None)
    disableAutoIndexGenLock=pset(False)
    nct=pset(1)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"MuTect2")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsbamtrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamtrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsponstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("ponstrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreferenceFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("referenceFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsinputNormalFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputNormalFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsinputTumorFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputTumorFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsnct(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("nct", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsveptrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("veptrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssnpstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("snpstrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputFile"):
            outputValue=getattr(self,"outputFile")
        self.send("outputFile", outputValue)
