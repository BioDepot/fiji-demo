# Pull base JDK-7 image.
FROM openjdk:7
ENV PATH $PATH:/usr/local/bin/Fiji.app
ADD Fiji.app /usr/local/bin/Fiji.app

