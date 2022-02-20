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

class OWbiobambam2(OWBwBWidget):
    name = "biobambam2"
    description = "Convert bam files to fastq"
    priority = 20
    icon = getIconName(__file__,"biobambam.png")
    want_main_area = False
    docker_image_name = "biodepot/biobambam2"
    docker_image_tag = "2.0.179__debian_bullseye-slim__4a043589"
    inputs = [("inputFile",str,"handleInputsinputFile"),("trigger",str,"handleInputstrigger"),("outputDir",str,"handleInputsoutputDir"),("firstmates",str,"handleInputsfirstmates"),("secondmates",str,"handleInputssecondmates"),("ufirstmates",str,"handleInputsufirstmates"),("usecondmates",str,"handleInputsusecondmates"),("singleend",str,"handleInputssingleend"),("bypass",str,"handleInputsbypass")]
    outputs = [("outputDir",str),("inputFile",str),("outputfiles",str),("triggerOut",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    inputFile=pset([])
    outputDir=pset([])
    collate=pset(False)
    combs=pset(False)
    inputformat=pset("bam")
    reference=pset(None)
    ranges=pset(None)
    exclude=pset("SECONDARY,SUPPLEMENTARY")
    disablevalidation=pset(False)
    colhlog=pset(18)
    colsbs=pset(33554432)
    tempfilename=pset(None)
    gz=pset(False)
    ziplevel=pset(None)
    fasta=pset(False)
    inputbuffersize=pset(None)
    firstmates=pset([])
    secondmates=pset([])
    ufirstmates=pset([])
    usecondmates=pset([])
    singleend=pset([])
    outputperreadgroup=pset(False)
    outputperreadgroupsuffixF=pset(None)
    outputperreadgroupsuffixF2=pset(None)
    outputperreadgroupsuffixO=pset(None)
    outputperreadgroupsuffixO2=pset(None)
    outputperreadgroupsuffixS=pset(None)
    tryoq=pset(False)
    split=pset(False)
    splitprefix=pset(False)
    tags=pset(None)
    outputperreadgrouprgsm=pset(False)
    outputperreadgroupprefix=pset(None)
    alignmentFlags=pset(None)
    bypass=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"biobambam2")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsinputFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("inputFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfirstmates(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("firstmates", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssecondmates(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("secondmates", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsufirstmates(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("ufirstmates", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsusecondmates(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("usecondmates", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssingleend(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("singleend", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsbypass(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("bypass", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputDir"):
            outputValue=getattr(self,"outputDir")
        self.send("outputDir", outputValue)
        outputValue=None
        if hasattr(self,"inputFile"):
            outputValue=getattr(self,"inputFile")
        self.send("inputFile", outputValue)
        outputValue=None
        if hasattr(self,"outputfiles"):
            outputValue=getattr(self,"outputfiles")
        self.send("outputfiles", outputValue)
        outputValue=None
        if hasattr(self,"triggerOut"):
            outputValue=getattr(self,"triggerOut")
        self.send("triggerOut", outputValue)
