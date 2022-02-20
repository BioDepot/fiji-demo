#!/bin/bash
if [ -z "$bypass" ]; then
	bamtofastq $@
else
	echo Bypassing biobambam2
fi
exit $?
