#!/bin/bash

TARGET_DIR="fiji_workflow/widgets/fiji_workflow/fiji/Dockerfiles"

IMAGE_TAG="biodepot/fiji:latest"

if [ "$EUID" -ne 0 ]
then
    echo "=============================================="
    echo "Warning: this script is not being run as root."
    echo "You may experience an error with Docker, as the daemon socket is usually owned by root."
    echo "If this occurs, run this script as root or use \`sudo\`."
    echo "=============================================="
    sleep 5
fi
echo ""
    
if [ ! -d "$TARGET_DIR" ]
then
    echo "Error: fiji_workflow directory missing!"
    echo "This likely means this script is not being run from the top-level directory of the repository."
    exit 1
fi

if [ ! -d "$TARGET_DIR/Fiji.app" ]; then
    echo "Fiji.app directory does not exist! Downloading FIJI..."
    wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip -O $TARGET_DIR/fiji-linux64.zip
    unzip $TARGET_DIR/fiji-linux64.zip -d $TARGET_DIR
    rm -rf $TARGET_DIR/fiji-linux64.zip
fi
echo ""

echo "Updating FIJI..."
$TARGET_DIR/Fiji.app/ImageJ-linux64 --update update
echo ""

echo "Building Docker image $IMAGE_TAG..."
docker build -t $IMAGE_TAG $TARGET_DIR
echo ""
