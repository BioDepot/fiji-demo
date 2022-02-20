#!/bin/bash
if [ -z ${prefix+x} ]; then
	baseFile=$reference
else
	baseFile=$prefix
fi

indexExists() {
	for ex in `echo amb ann bwt pac sa`; do
		echo "Checking for ${baseFile}.$ex"
		[[ ! -f ${baseFile}.64.$ex && ! -f ${baseFile}.$ex ]] && return 1
	done
	return 0
}

if indexExists && [[ -z "${overwrite}" ]]; then
	echo "reference exists and will not overwrite"
	exit 0
fi

cmd="bwa index $@"
echo $cmd
$cmd

# cannot trust return code on this from github issue - if the SA file is constructed then it probably is OK
indexExists
exit $?
