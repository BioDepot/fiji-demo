# Pull Ubuntu 20.04 LTS image.
FROM ubuntu:20.04
# Install JDK and some system tools.
RUN apt-get -y update && apt-get -y install default-jdk wget unzip

# Download a copy of Fiji
RUN wget https://downloads.imagej.net/fiji/latest/fiji-linux64.zip -O /tmp/fiji-linux64.zip
# Unzip Fiji and delete the zip file so it doesn't take up space in the image
RUN unzip /tmp/fiji-linux64.zip -d /usr/local/bin/ && rm -rf /tmp/fiji-linux64.zip

# Add the BigStitcher update site
RUN /usr/local/bin/Fiji.app/ImageJ-linux64 --update add-update-site BigStitcher \
    https://sites.imagej.net/BigStitcher
# Update Fiji
RUN /usr/local/bin/Fiji.app/ImageJ-linux64 --update update

# Add Fiji directory to $PATH
ENV PATH $PATH:/usr/local/bin/Fiji.app
# Add startfiji.sh wrapper script for starting Fiji from Bwb
ADD startfiji.sh /usr/local/bin/startfiji.sh
