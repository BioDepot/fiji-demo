FROM mgibio/pindel:v0.2.5b8
MAINTAINER Hong Hung
COPY sambamba-0.7.0-linux-static /usr/local/bin/sambamba
COPY generate_bam_config.sh /usr/local/bin/generate_bam_config.sh
RUN apt-get update && apt-get install -y jq && apt-get clean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 
COPY pindel2vcf /usr/local/bin/pindel2vcf
RUN ln -s /usr/local/bin/pindel2vcf /usr/local/bin/pindel2vcftcga
COPY somatic_indelfilter.pl /usr/local/bin/somatic_indelfilter.pl
COPY run_pindel.sh /usr/local/bin/run_pindel.sh
RUN  chmod +x /usr/local/bin/*
ENTRYPOINT []
