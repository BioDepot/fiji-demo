# Pull base JDK-7 image.
FROM openjdk:7
ENV PATH $PATH:/usr/local/bin/Fiji.app
COPY Fiji-jdk7 /usr/local/bin/Fiji.app

