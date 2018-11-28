#!/bin/bash

root=$1
echo $root
first=$2
echo $first
last=$3
echo $last
#length = 2

for i in $(seq $first $last); do python ~/Téléchargements/tz/createepun.py "$root/$i"; done
#for i in $(seq first last); do python ~/Téléchargements/tz/createepun.py "https://www.japscan.cc/lecture-en-ligne/kingdom/$i"; done
