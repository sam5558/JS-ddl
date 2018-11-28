# Created by fadeos and sam5558

#!/bin/bash

root=$1
first=$2
last=$3

for i in $(seq $first $last); do python createcbz.py "$root/$i"; done
