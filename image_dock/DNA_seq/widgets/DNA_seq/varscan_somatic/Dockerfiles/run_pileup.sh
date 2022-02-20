#!/bin/bash
if [ -z $reverse_order ]; then
 echo "samtools mpileup $@"
 samtools mpileup $@
else
 normal="${@: -1}"
 set -- "${@:1:$(($#-1))}"
 tumor="${@: -1}"
 set -- "${@:1:$(($#-1))}"
  echo "samtools mpileup $@ $normal $tumor"
  samtools mpileup $@ $normal $tumor
fi
