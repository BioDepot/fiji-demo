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

class OWSomaticSniper(OWBwBWidget):
    name = "SomaticSniper"
    description = "Somatic sniper variant caller"
    priority = 50
    icon = getIconName(__file__,"somatic_sniper.png")
    want_main_area = False
    docker_image_name = "biodepot/somatic-sniper"
    docker_image_tag = "1.0.5.0__buster-slim__0d291126"
    inputs = [("inputfiles",str,"handleInputsinputfiles"),("Trigger",str,"handleInputsTrigger"),("reference",str,"handleInputsreference"),("output",str,"handleInputsoutput")]
    outputs = [("OutputDir",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    reference=pset(None)
    minmapq=pset(None)
    minsnvq=pset(None)
    lohreport=pset(False)
    gorreport=pset(False)
    nopriors=pset(False)
    usepriors=pset(False)
    priorprob=pset(None)
    theta=pset(None)
    haplotypes=pset(None)
    priordiff=pset(None)
    normalid=pset(None)
    tumorid=pset(None)
    format=pset(None)
    inputfiles=pset([])
    output=pset([])
    reverse_order=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"SomaticSniper")) as f:
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
    def handleInputsreference(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutput(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("output", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"OutputDir"):
            outputValue=getattr(self,"OutputDir")
        self.send("OutputDir", outputValue)
