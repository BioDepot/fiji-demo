FROM alpine:3.13.2 as builder
RUN apk add --update --no-cache binutils g++ make zlib-dev
RUN wget -O- https://github.com/danielfan/MuSE/archive/v1.0-rc.tar.gz | tar xzf - \
	&& cd MuSE-1.0-rc \
	&& make \
	&& strip MuSE

FROM alpine:3.13.2
MAINTAINER Hong Hung
RUN apk add --update --no-cache bash libstdc++
COPY --from=builder /MuSE-1.0-rc/MuSE /usr/local/bin/muse
COPY run_muse_call.sh /usr/local/bin/run_muse_call.sh
