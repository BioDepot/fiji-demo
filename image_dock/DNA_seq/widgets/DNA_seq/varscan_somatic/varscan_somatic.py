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

class OWvarscan_somatic(OWBwBWidget):
    name = "varscan_somatic"
    description = "Varscan2 somatic cell variant caller using mpileup"
    priority = 56
    icon = getIconName(__file__,"varscan.png")
    want_main_area = False
    docker_image_name = "biodepot/varscan-samtools"
    docker_image_tag = "2.3.9__1.12__jdk-15.0.1_9-alpine"
    inputs = [("inputfiles",str,"handleInputsinputfiles"),("outputsnp",str,"handleInputsoutputsnp"),("outputindel",str,"handleInputsoutputindel")]
    outputs = [("output",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    inputfiles=pset([])
    outputbase=pset(None)
    outputsnp=pset([])
    outputindel=pset([])
    mincoverage=pset(None)
    mincoveragenorm=pset(None)
    mincoveragetum=pset(None)
    minvarfreq=pset(None)
    minhomfreq=pset(None)
    tumorpurity=pset(None)
    normalpurity=pset(None)
    pvalue=pset(None)
    somaticpvalue=pset(None)
    strandfilter=pset(False)
    validation=pset(False)
    outputvcf=pset(False)
    mintumor=pset(None)
    minnormal=pset(None)
    hvpvalue=pset(None)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"varscan_somatic")) as f:
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
    def handleInputsoutputsnp(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputsnp", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutputindel(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outputindel", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"output"):
            outputValue=getattr(self,"output")
        self.send("output", outputValue)
