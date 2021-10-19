# Workflow with Fiji widget

## Building `biodepot/fiji` Docker image
This repository contains the Dockerfile and other files used to build
the `biodepot/fiji` image; they are located in
`fiji_workflow/widgets/fiji_workflow/fiji/Dockerfiles`. They include
the Dockerfile itself and the `startfiji.sh` wrapper script that is
used to launch Fiji from Bwb. Additionally, a copy of Fiji should be
in this directory to be added to the Docker image, but it is not
included in the repository checkout.

The script `build_docker_image.sh` will take care of downloading and
updating a copy of Fiji to be placed into the Docker container, and
then will build and tag the `biodepot/fiji` Docker image.

To update the `biodepot/fiji` image, run `sudo
./build_docker_image.sh` *from the top-level directory* of the
repository. (`sudo` is needed because by default the Docker daemon
socket is owned by `root`.)
