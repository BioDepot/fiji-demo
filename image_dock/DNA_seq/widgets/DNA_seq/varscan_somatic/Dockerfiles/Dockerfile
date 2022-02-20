FROM adoptopenjdk/openjdk15:jdk-15.0.1_9-alpine
MAINTAINER Hong Hung
RUN wget -O VarScan https://sourceforge.net/projects/varscan/files/VarScan.v2.3.9.jar/download
RUN apk add zlib libbz2 libcurl xz-libs ncurses-dev bash
COPY --from=biodepot/bwa-samtools:gdcalign__alpine_3.12__10034cca \
    /usr/local/bin/samtools /usr/local/bin/samtools
COPY run_somatic.sh /usr/local/bin/run_somatic.sh
COPY run_pileup.sh /usr/local/bin/run_pileup.sh
