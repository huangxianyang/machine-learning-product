#!/bin/bash
ENVT=$1

TARGETS=("/root/mlModel/web/Server.py")
for target in "${TARGETS[@]}"
do
     pkill -f $target
     echo "killing process $target"
done