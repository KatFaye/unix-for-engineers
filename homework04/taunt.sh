#!/bin/sh
# SLEEPER-esque program.
#Author: Kat Herring
 
secs=10
endTime=$(($(date +%s) + secs )) #endtime

./fortune | ./cowsay

trap  ' ./cowsay "Why does it take a minute to say hello and forever to say goodbye? You shall go far, $USER." ; exit' 1
trap  ' ./cowsay "Curiousity killed the cat, but satisfaction brought me back!" ; exit' 2 15

while [ $(date +%s) -lt $endTime ]; do
sleep 1 
done

./cowsay "...And so I close now, realizing that the ending has not yet been written."
exit 0


