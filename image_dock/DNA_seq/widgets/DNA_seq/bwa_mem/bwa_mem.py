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

class OWbwa_mem(OWBwBWidget):
    name = "bwa_mem"
    description = "Aligns paired-end sequences, sort and return bam files"
    priority = 30
    icon = getIconName(__file__,"bwasamsort.png")
    want_main_area = False
    docker_image_name = "biodepot/bwa-samtools-gdc"
    docker_image_tag = "0.7.15__1.9.52__alpine_3.12__da70fa5a"
    inputs = [("fastq_files",str,"handleInputsfastq_files"),("readgroup",str,"handleInputsreadgroup"),("reference",str,"handleInputsreference"),("fastq_trigger",str,"handleInputsfastq_trigger"),("reference_trigger",str,"handleInputsreference_trigger"),("outputfiles",str,"handleInputsoutputfiles"),("threads",str,"handleInputsthreads")]
    outputs = [("outputfiles",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    readgroup=pset([])
    reference=pset(None)
    fastq_files=pset([])
    threads=pset(None)
    minscore=pset(None)
    outputfiles=pset([])
    addrg=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"bwa_mem")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsfastq_files(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastq_files", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreadgroup(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("readgroup", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsfastq_trigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("fastq_trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsreference_trigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("reference_trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputfiles(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputfiles", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsthreads(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("threads", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"outputfiles"):
            outputValue=getattr(self,"outputfiles")
        self.send("outputfiles", outputValue)
