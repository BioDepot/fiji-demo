#!/bin/bash
outputfile="${@: -1}"
#remove last element from parameters
set -- "${@:1:$(($#-1))}"

bqsrfile=${outputfile%.*}_bqsr.grp
echo "java -jar /usr/GenomeAnalysisTK.jar -T BaseRecalibrator -knownSites $snps $@ -o $bqsrfile"
java -jar /usr/GenomeAnalysisTK.jar -T BaseRecalibrator -knownSites $snps $@ -o $bqsrfile
echo "java -jar /usr/GenomeAnalysisTK.jar -T PrintReads $@ --BQSR $bqsrfile -o $outputfile"
java -jar /usr/GenomeAnalysisTK.jar -T PrintReads $@ --BQSR $bqsrfile -o $outputfile
