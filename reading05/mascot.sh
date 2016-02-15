#!/bin/bash
#Checks output of uname and prints response

case $(uname) in 

Linux ) echo "Tux"
;;
Darwin ) echo "Hexley"
;;
FreeBSD | NetBSD | OpenBSD ) echo "Beastie"

esac
