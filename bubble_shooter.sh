#!/bin/bash

##
## Bubble-Shooter
## File description:
## bubble_shooter.sh
##

function cat_readme() {
    echo "Usage: ./cat_readme.sh [OPTION]..."
    echo "Launch bubble shooter game made in python with pygame-ce."
    echo ""
    echo "Options:"
    echo "  -h, --help      Display this help and exit."
}

if [ $# -eq 0 ]; then
  ./src/main.py

elif [ $# -eq 1 ] && [ "$1" == "-h" ] ; then
  cat_readme

else
  echo "error: invalid option."
  exit 84
fi