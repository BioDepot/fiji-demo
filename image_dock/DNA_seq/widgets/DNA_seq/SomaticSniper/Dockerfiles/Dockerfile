FROM debian:buster-slim AS builder
RUN apt-get update && apt-get install -y build-essential git-core cmake zlib1g-dev libncurses-dev wget
RUN wget -c https://github.com/genome/somatic-sniper/archive/v1.0.5.0.tar.gz -O - | tar -xz
RUN cd somatic-sniper* && cmake . && make deps && make -j && make install

FROM debian:buster-slim
MAINTAINER Hong Hung
COPY --from=builder /usr/local/bin/bam-somaticsniper /usr/local/bin/bam-somaticsniper
RUN mkdir -p /usr/local/share/doc/somatic-sniper-1.0.5.0
COPY --from=builder /somatic-sniper-1.0.5.0/docs/copyright \
    /usr/local/share/doc/somatic-sniper-1.0.5.0/copyright
COPY run_sniper.sh /usr/local/bin/run_sniper.sh
