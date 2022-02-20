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

class OWPindel(OWBwBWidget):
    name = "Pindel"
    description = "Pindel somatic variant caller with merge function as per GDC"
    priority = 74
    icon = getIconName(__file__,"pindel.png")
    want_main_area = False
    docker_image_name = "biodepot/pindel-gdc"
    docker_image_tag = "0.2.5b8__10f065ec"
    inputs = [("bamconfigfile",str,"handleInputsbamconfigfile"),("reference",str,"handleInputsreference"),("Trigger",str,"handleInputsTrigger"),("prefix",str,"handleInputsprefix"),("nthreads",str,"handleInputsnthreads")]
    outputs = [("prefix",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    reference=pset(None)
    prefix=pset([])
    bamconfigfile=pset([])
    pindelinputlfile=pset(None)
    pindelconfiglfile=pset(None)
    chromosome=pset(None)
    readpair=pset(True)
    mindist=pset(None)
    nthreads=pset(None)
    maxrange=pset(None)
    windowsize=pset(None)
    errorrate=pset(None)
    sensitivity=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"Pindel")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsbamconfigfile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bamconfigfile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsprefix(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("prefix", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsnthreads(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("nthreads", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"prefix"):
            outputValue=getattr(self,"prefix")
        self.send("prefix", outputValue)
