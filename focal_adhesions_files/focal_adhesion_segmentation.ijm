startTime = getTime();

// Open image
open("/data/Paxillin_test_set.tif");

// Subtract background
print("Subtracting background...");
run("Subtract Background...", "rolling=50 sliding stack");

// Enhance local contrast (have to do this per slice since the CLAHE plugin doesn't
//  seem to support batch processing on stacks)
Stack.getDimensions(width, height, channels, slices, frames);
for (i = 1; i <= slices; i++) {
    setSlice(i);
    print("Enhancing local contrast (" + i + "/" + slices + ")...");
    run("Enhance Local Contrast (CLAHE)", "blocksize=19 histogram=256 maximum=6 mask=*None* fast_(less_accurate)");
}

// Exponentiation
print("Applying mathematical exponentiation...")
run("Exp", "stack");

// Enhance brightness and contrast
print("Enhancing brightness and contrast...")
run("Enhance Contrast", "saturated=0.35");
run("Apply LUT", "stack");

// Apply LoG 3D filter
print("Applying Laplacian of Gaussians (LoG)...")
// LoG 3D processes asynchronously; rather than blocking, execution will move on
//  to the next command, and a window titled "LoG of <image title>" will appear later. 
//  To deal with this we have to continuously check for the "LoG of <title>" window, 
//  which will block until it is available.
title=getTitle();
run("LoG 3D", "sigmax=5 sigmay=5 displaykernel=0 volume=0");
while(!isOpen("LoG of " + title)){

}
selectWindow("LoG of " + title);

// Threshold
print("Thresholding...");
run("8-bit");
setAutoThreshold("Default");
run("Convert to Mask", "method=Default background=Light calculate black");

// Analyze particles
print("Analyzing particles...");
// make sure that we output the desired measurements 
//  (fitting elipse, area, centroid coordinates, slice number)
run("Set Measurements...", "area centroid fit stack redirect=None decimal=4");
run("Analyze Particles...", "size=50-infinity circularity=0.00-0.99 show=Outlines display clear stack");

print("Saving results...");
saveAs("Results", "/data/Results.csv");

duration = getTime() - startTime;
print("Done in " + duration/1000 + " seconds! Exiting...");
run("Quit");
