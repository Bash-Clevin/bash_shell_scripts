#!/usr/bin/bash

echo "Input url "
read url

echo $(cd ~/storage/music) && { youtube-dl -o '/data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s' --ignore-config --extract-audio --embed-thumbnail --audio-format mp3 --audio-quality 0  $url; cd -;}

