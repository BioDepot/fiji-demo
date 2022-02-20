#!/bin/bash
echo "java -jar /usr/GenomeAnalysisTK.jar -T IndelRealigner $@"
java -jar /usr/GenomeAnalysisTK.jar -T IndelRealigner "$@"
