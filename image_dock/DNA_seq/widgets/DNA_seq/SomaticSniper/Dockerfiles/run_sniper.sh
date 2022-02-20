#!/bin/bash
if [ -z $reverse_order ]; then
  cmd="bam-somaticsniper $@"
else
  output="${@: -1}"
  set -- "${@:1:$(($#-1))}"
  tumor="${@: -1}"
  set -- "${@:1:$(($#-1))}"
  normal="${@: -1}"
  set -- "${@:1:$(($#-1))}"
  cmd="bam-somaticsniper $@ $tumor $normal $output"
fi
echo "$cmd"
$cmd
