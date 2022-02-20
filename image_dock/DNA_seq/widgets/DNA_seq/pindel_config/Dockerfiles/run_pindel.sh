#!/bin/bash
somatic_config=${prefix}.somatic_config
merged_output=${prefix}.merged
echo "pindel $@"
pindel $@

fgrep -h ChrID ${prefix}_D ${prefix}_SI > $merged_output

echo "indel.filter.input = $merged_output" > $somatic_config
echo "indel.filter.vaf = 0.08" >> $somatic_config
echo "indel.filter.cov = 20" >> $somatic_config
echo "indel.filter.hom = 6" >> $somatic_config
echo 'indel.filter.pindel2vcf = /usr/local/bin/pindel2vcf' >> $somatic_config
echo "indel.filter.reference =  $reference" >> $somatic_config
echo "indel.filter.referencename = GRCh38" >> $somatic_config
echo "indel.filter.referencedate = $(date '+%Y%m%d')"  >> $somatic_config
echo "indel.filter.output = ${prefix}.vcf " >> $somatic_config
cat $somatic_config
echo "somatic_indelfilter.pl $somatic_config"
somatic_indelfilter.pl $somatic_config

