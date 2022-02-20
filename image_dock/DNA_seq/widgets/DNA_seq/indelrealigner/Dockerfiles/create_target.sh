#/bin/bash

echo "$@"
bamstr=$(echo $bamfiles | sed  's/\"//g' | sed 's/\[//g' | sed 's/\]//g' | sed 's/\,/ -I /g') 
echo "java -jar /usr/GenomeAnalysisTK.jar -T RealignerTargetCreator $@ -I $bamstr"
java -jar /usr/GenomeAnalysisTK.jar -T RealignerTargetCreator $@ -I $bamstr
