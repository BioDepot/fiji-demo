#!/bin/bash
if [ -z $reverse_order ]; then
	cmd="muse call $@"
else
	tumor="${@: -1}"
	set -- "${@:1:$(($#-1))}"
	normal="${@: -1}"
	set -- "${@:1:$(($#-1))}"
	cmd="muse call $@ $tumor $normal"
fi
echo $cmd
$cmd
exit $?
