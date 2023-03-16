#!/bin/bash

if [ ! -e "$1" ]; then
  
  echo "2"
elif [ -s "$1" ]; then
  
  echo "0"
else
  
  echo "1"
fi
