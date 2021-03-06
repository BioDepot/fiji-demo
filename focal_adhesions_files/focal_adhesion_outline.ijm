// Open image
dataset = getArgument;
if (dataset=="") dataset="/data/fiji-test/Paxillin_test_set.tif";
open(dataset);
setAutoThreshold("Default dark");
run("Convert to Mask", "method=Default background=Dark calculate black");
run("Options...", "iterations=3 count=1 black do=Nothing");
run("Dilate", "stack");
run("Close-", "stack");
run("Fill Holes", "stack");
// perform 4 iterations of erosion to get rid of noise
run("Options...", "iterations=4 count=1 black do=Nothing");
run("Erode", "stack");
run("Outline", "stack");
run("Save XY Coordinates...", "background=0 process save=/data/border.txt");
