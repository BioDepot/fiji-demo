FROM ubuntu:latest
RUN apt-get -y update && apt-get -y install default-jdk
ENV PATH $PATH:/usr/local/bin/Fiji.app
ADD Fiji.app /usr/local/bin/Fiji.app
ADD startfiji.sh /usr/local/bin/startfiji.sh
ADD run_segmentation.py /usr/local/bin/run_segmentation.py
