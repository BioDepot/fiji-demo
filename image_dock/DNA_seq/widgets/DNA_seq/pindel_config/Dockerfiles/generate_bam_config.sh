#!/bin/bash

bamfiles=( $(echo $BAMFILES | jq -r '.[]') )
tagfiles=( $(echo $TAGS | jq -r '.[]') )
i=0
    mean=$(samtools view -f66 ${bamfiles[$i]} | head -n 10000 | awk 'function abs(x){return (x < 0) ? -x : x;} BEGIN {FS="\t"}; {sum+=abs($9)} END {print sum/NR}')
    echo "${bamfiles[$i]}"$'\t'"$mean"$'\t'"${tagfiles[$i]}" > $configfile
for ((i=1; i<${#bamfiles[@]}; i++)); do
    mean=$(samtools view -f66 ${bamfiles[$i]} | head -n 10000 | awk 'function abs(x){return (x < 0) ? -x : x;} BEGIN {FS="\t"}; {sum+=abs($9)} END {print sum/NR}')
    echo "${bamfiles[$i]}"$'\t'"$mean"$'\t'"${tagfiles[$i]}" >> $configfile
done
#

