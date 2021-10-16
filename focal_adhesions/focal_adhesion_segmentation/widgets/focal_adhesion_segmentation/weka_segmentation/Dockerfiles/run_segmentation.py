import os
from ij import IJ, ImagePlus
from ij.io import FileSaver
from trainableSegmentation import WekaSegmentation
from trainableSegmentation.utils import Utils
from java.lang import System

classifier_file = os.getenv("classifier")
image_file = os.getenv("image")
output_file = os.getenv("output")

IJ.log("loading image " + image_file);
image = IJ.openImage(image_file)

segmenter = WekaSegmentation(image)
IJ.log("loading classifier " + classifier_file)
segmenter.loadClassifier(classifier_file)
IJ.log("running classifier")
segmenter.applyClassifier(False)
result = segmenter.getClassifiedImage()
result.setLut(Utils.getGoldenAngleLUT())
segmenter.shutDownNow()

IJ.log("done, saving image " + output_file)
FileSaver(result).saveAsTiff(output_file)
System.exit(0)
