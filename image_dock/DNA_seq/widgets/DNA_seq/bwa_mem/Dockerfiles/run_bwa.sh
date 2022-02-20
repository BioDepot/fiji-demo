#!/bin/bash
function findrg(){
	tab='\t'
	filebase=$(basename -- "$outputfile")
	idstr="${filebase%.*}".1
	smstr="${filebase%.*}"
	libstr="${filebase%.*}"_lib
	plstr="ILLUMINA"
	extension="${filename##*.}"
	if [ $extension == 'gz' ]; then
		header=$(zcat $filename | head -n 1)
	else
		header=$(head -1 $filename)
	fi
	echo $header

	#new illumina have two fields
	fields=(${header:1})
	seqid=${fields[0]}
	seqid_fields=(${seqid//:/ })
	if [[ (( ${#seqid_fields[@]} == 5 )) || (( ${#seqid_fields[@]} == 7 )) ]]; then
		echo "extracting read group fields"
		idstr=${seqid:0:5}."${seqid_fields[1]}"
		echo "$idstr"
		pustr=${seqid_fields[0]}."${seqid_fields[1]}"
		rgstr="@RG${tab}ID:$idstr${tab}PU:$pustr${tab}SM:$smstr${tab}LB:$libstr${tab}PL:$plstr"
	else
		rgstr="@RG${tab}ID:$idstr${tab}SM:$smstr${tab}LB:$libstr${tab}PL:$plstr"
	fi
}

#last argument has outputfile
outputfile="${@: -1}"
#remove last element from parameters
set -- "${@:1:$(($#-1))}"
if [ -n $addrg ]; then
	filename="${@: -1}"
	findrg
	cmd="bwa mem -R \"$rgstr\" $@ | samtools sort -o $outputfile"
else
	cmd="bwa mem $@ | samtools sort -o $outputfile"
fi
echo $cmd
# if either bwa or samtools fails return an error status
set -o pipefail
eval $cmd
exit $?
