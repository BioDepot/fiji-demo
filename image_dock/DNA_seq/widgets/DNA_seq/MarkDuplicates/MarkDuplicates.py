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

class OWMarkDuplicates(OWBwBWidget):
    name = "MarkDuplicates"
    description = "Mark duplicates"
    priority = 35
    icon = getIconName(__file__,"gatk-mark-dupes.png")
    want_main_area = False
    docker_image_name = "biodepot/gatk"
    docker_image_tag = "4.1.9.0__openjdk_8-jre-alpine__cb1b2f17"
    inputs = [("inputFile",str,"handleInputsinputFile"),("trigger",str,"handleInputstrigger"),("outputFile",str,"handleInputsoutputFile"),("metricsFile",str,"handleInputsmetricsFile")]
    outputs = [("outputFile",str),("metricsFile",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    inputFile=pset([])
    argumentsFile=pset([])
    assumeSortOrder=pset(None)
    barcodeTag=pset(None)
    clearDt=pset(None)
    markDupesComments=pset([])
    duplexUmi=pset(None)
    duplicateScoringStragety=pset(None)
    maxFileHandlesForReadEndsMap=pset(None)
    maxOpticalDuplicateSetSize=pset(None)
    molecularIdentifierTag=pset(None)
    opticalDuplicatePixelDistance=pset(None)
    programGroupCommandLine=pset(None)
    programGroupName=pset(None)
    programGroupVersion=pset(None)
    programRecordId=pset(None)
    readNameRegex=pset(None)
    readOneBarcodeTag=pset(None)
    readTwoBarcodeTag=pset(None)
    removeDuplicates=pset(None)
    removeSequencingDuplicates=pset(None)
    sortingCollectionSizeRatio=pset(None)
    tagDuplicateSetMembers=pset(None)
    taggingPolicy=pset(None)
    addPgTagToReads=pset(None)
    compressionLevel=pset(None)
    createIndex=pset(None)
    createMd5File=pset(None)
    ga4ghClientSecrets=pset(None)
    maxRecordsInRam=pset(None)
    markDupesQuiet=pset(None)
    referenceSequence=pset(None)
    tmpDir=pset([])
    useJdkDeflater=pset(None)
    useJdkInflater=pset(None)
    validationStringency=pset(None)
    verbosity=pset(None)
    showHidden=pset(None)
    outputFile=pset([])
    metricsFile=pset([])
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"MarkDuplicates")) as f:
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
    def handleInputsoutputFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsmetricsFile(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("metricsFile", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputFile"):
            outputValue=getattr(self,"outputFile")
        self.send("outputFile", outputValue)
        outputValue=None
        if hasattr(self,"metricsFile"):
            outputValue=getattr(self,"metricsFile")
        self.send("metricsFile", outputValue)
