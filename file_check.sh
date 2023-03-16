#!/bin/bash

if [ ! -e "$1" ]; then
  # file does not exist
  echo "2"
elif [ -s "$1" ]; then
  # file exists and is not empty
  echo "0"
else
  # file exists but is empty
  echo "1"
fi
