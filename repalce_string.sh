#!/bin/bash

V_1=$(grep "jane " ../data/list.txt | cut -d ' ' -f 3)

for i in $V_1; do 
  i="../$i" 
  echo $i
  if [ -e "$i" ]; then
    echo "$i" >> oldFiles.txt
  else
    echo "File doesn't exist"
  fi
done

