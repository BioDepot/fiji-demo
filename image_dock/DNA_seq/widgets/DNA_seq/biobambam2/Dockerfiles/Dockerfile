FROM debian:bullseye-slim
RUN apt-get update \
	&& apt-get install -y --no-install-recommends biobambam2 \
	&& rm -rf /var/lib/apt/lists/*
COPY bamtofastq.sh /usr/local/bin/
