#!/bin/bash
pileup="${@: -1}" 
set -- "${@:1:$(($#-1))}"
echo "java -jar VarScan somatic  $pileup $outputbase --mpileup 1 $@"
java -jar VarScan somatic  $pileup $outputbase --mpileup 1 $@

#find the names of the outputfiles
if [ -z $outputsnp ]; then
  outputsnp="$(dirname ${pileup})/${outputbase}.snp"
fi
if [ -z $outputindel ]; then
 outputindel="$(dirname ${pileup})/${outputbase}.indel"
fi

options_string=""
if [ -n "$mintumor" ]; then
 options_string="$options_string --min-tumor-freq $mintumor"
fi
if [ -n "$minnormal" ]; then 
 options_string="$options_string --min-normal-freq $minnormal"
fi
if [ -n "$hvpvalue" ]; then 
 options_string="$options_string --p-value $hvpvalue"
fi

echo "java -jar VarScan processSomatic $outputsnp $options_string"
java -jar VarScan processSomatic $outputsnp $options_string
echo "java -jar VarScan processSomatic $outputindel $options_string"
java -jar VarScan processSomatic $outputindel $options_string
