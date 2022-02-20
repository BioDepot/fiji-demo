FROM biodepot/bwb:latest
ENV custom=/image_dock
ADD image_dock /image_dock
RUN generate_setup.sh
RUN rm -r /image_dock
