# Image Analysis and Processing with Fiji in Bwb

This repository contains several workflows for
[Bwb](https://github.com/BioDepot/Biodepot-workflow-builder) that
demonstrate integration of image processing and analysis in
[Fiji](https://fiji.sc) with other tools for processing and analysis,
such as Jupyter Notebooks.

The `fiji_workflow` directory is a Bwb workflow containing a widget
for Fiji; the widget has options for executing ImageJ scripts or
macros, opening images, and accepting additional plugins at
runtime. The user can additionally choose to use their own
installation of Fiji rather than the default, which is provided as a
Docker container.

Additionally, There are two sample workflows provided; one performs
segmentation and analysis of focal adhesions in a sample set of
images, while the other performs _TODO (Shishir): write what the
BigStitcher workflow does_.

# Usage
## Opening the Workflows

First, clone this repository with `git clone
https://github.com/BioDepot/fiji-demo`.

Then, enter the cloned repository:
```bash
cd fiji-demo
```

and run Bwb in this directory with
```bash
sudo docker run --rm \
 -p 5900:5900 -p 6080:6080 \
 -v ${PWD}/:/data \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 --privileged --group-add root \
 biodepot/bwb
 ```
 
Now, open Bwb either in the browser or a VNC client (see [Running
Bwb](https://github.com/biodepot/biodepot-workflow-builder#overview-running-bwb)
in the Bwb documentation) and select `File > Load Workflow`; navigate
to `/data/workflows` and choose one of the workflows in that directory
to open. Please read further for more details on each of the
workflows.

## `fiji_workflow` - Fiji Widget
The `fiji_workflow` provides the base Fiji widget used in the sample
workflows. To use it, you can copy the `fiji_workflow` directory to
your own working directory, and then open this workflow in Bwb before
your own workflow to add the widget to the toolbox on the left.

The Fiji widget has a few parameters that can be set to use different
functionalities available in Fiji. 
![A screenshot of the Fiji widget, showing the different
options.](images/fiji_widget.png)
  * **`Fiji.app` directory** - the path to an alternative installation
    of Fiji, if desired. If not used, the read-only installation of
    Fiji provided with the `biodepot/fiji` Docker image will be used.
  * **Install Fiji to directory** - If provided, a path to a directory
    where Fiji should be installed. A `Fiji.app` directory will be
    created within the directory provided; this `Fiji.app` directory
    should be chosen as the "`Fiji.app` directory" above if you want
    to use the new installation of Fiji.
  * **Extra plugins directory** - If provided, a path to a directory
    containing extra plugins (in `.JAR` format) for Fiji; these
    plugins will be usable in macros and scripts. This is useful if
    your workflow depends on additional plugins that are not provided
    with the base distribution of Fiji, or whose licensing terms
    prohibit redistribution.
  * **Macro file** - If provided, a path to an [ImageJ
    macro](https://imagej.net/scripting/macro) file that should be
    executed when Fiji starts up. *Please note that only one of "Macro
    file" or "Script file" should be provided; the behavior when both
    are provided is undefined.*
  * **Script file** - If provided, a path to an [ImageJ
    script](https://imagej.net/scripting/) file that should be
    executed when Fiji starts up. *Please note that only one of "Macro
    file" or "Script file" should be provided; the behavior when both
    are provided is undefined.*
  * **Image file** - If provided, a path to an image that should be
    opened by Fiji when it starts up. Useful for displaying images at
    the end of a workflow, or passing an image as an argument to a
    macro/script.
  * **Overwrite existing `Fiji.app`** - When using the "Install Fiji
    to directory" option above, if this option is chosen, the Fiji
    installation will be overwritten with a fresh installation each
    time the widget is executed.
  * **Run Headless** - If chosen, runs Fiji in [Headless
    mode](https://imagej.net/learn/headless). Please note that some
    scripts (and most macros) will not work in Headless mode because
    they require graphical functions; see the Fiji/ImageJ
    documentation for more information.
	
  Please note that "Export graphics" should be checked to be able to
  use the Fiji graphical interface; after copying a Fiji widget to
  your own workflow, this option may become unchecked.

## `focal_adhesion_segmentation` - Focal Adhesion Segmentation and Analysis

This workflow implements focal adhesion segmentation using the
algorithm described by Horzum _et al._ (see
[Citations/Acknowledgements](#citationsacknowledgements)). To use it, open the workflow
using the process described in [Opening the
Workflows](#opening-the-workflows) above; once the workflow is open,
double-click the "Start" widget and press the blue "Start" button.

The workflow will create a directory called `fiji-test` inside the `/data` volume
(i.e. inside your clone of the repository), within which several files
will be created; the final results will be in the form of a Jupyter
notebook called `Results.ipynb`. Once the workflow is complete, a web
browser will be opened to display the notebook.

## `bigstitcher** - BigStitcher workflow

**TODO (Shishir): Add specific documentation for BigStitcher workflow**

# Citations/Acknowledgements

  * Algorithm for segmenting focal adhesions is adapted from Horzum
  _et al._:

    > Utku Horzum, Berrin Ozdil, & Devrim Pesen-Okvur (2014). Step-by-step
    > 	quantitative analysis of focal adhesions. MethodsX, 1, 56-59. (doi:
    > 	https://doi.org/10.1016/j.mex.2014.06.004)

  * LoG 3D plugin for ImageJ is [available
    here](http://bigwww.epfl.ch/sage/soft/LoG3D/), from Sage /et al./
    The plugin is not distributed with the workflow, but is downloaded
    by the user's computer at runtime.
	
    > D. Sage, F.R. Neumann, F. Hediger, S.M. Gasser, M. Unser,
    >     "Automatic Tracking of Individual Fluorescence Particles:
    >     Application to the Study of Chromosome Dynamics," IEEE
    >     Transactions on Image Processing, vol. 14, no. 9, pp. 1372-1383,
    >     September 2005.
  * Dataset used for focal adhesion analysis is the one given on the
    [Focal Adhesion Analysis Server](https://faas.bme.unc.edu/), from
    Berginski and Gomez:
	
    > Berginski ME, Gomez SM. (2013). The Focal Adhesion Analysis
    > 	Server: a web tool for analyzing focal adhesion
    > 	dynamics. F1000Research, 2:68 (doi:
    > 	https://doi.org/10.3410/f1000research.2-68.v1)
	
  * [BigStitcher](https://www.nature.com/articles/s41592-019-0501-0):

    > Hörl, D.et al.(2019).  Bigstitcher: reconstructing high-resolution
    >     image datasets of cleared and expanded samples. Nature
    >     Methods,16(9), 870–874.
  * Fiji:
  
    > Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V.,
    >   Longair, M., Pietzsch, T., … Cardona, A. (2012). Fiji: an
    >   open-source platform for biological-image analysis. Nature Methods,
    >   9(7), 676–682. doi:10.1038/nmeth.2019

