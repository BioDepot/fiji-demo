#!/bin/bash

if [ -n "$installfiji" ]; then
    dest="$installfiji/Fiji.app"
	if [ -d $dest ]; then
	   if [ -n "$overwrite" ]; then
	    rm -r "$dest"
	    echo "installing Fiji.app to $dest"
		cp -r /usr/local/bin/Fiji.app $dest
	   else
	    echo "$dest exists - will not overwrite unless the overwrite option is checked"
	   fi 
	else
	  echo "installing Fiji.app to $dest"
	  cp -r /usr/local/bin/Fiji.app $dest
	fi
fi
echo "Command-line options: $@"
if [ -n "$fijidir" ]; then
	exec "$fijidir/ImageJ-linux64" "$@"
else
    echo "Running read-only copy of ImageJ/fiji"
    ImageJ-linux64 "$@"
fi
