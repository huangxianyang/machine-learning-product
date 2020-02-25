#!/bin/bash
ENVT=$1
COMPONENTS=$2


TARGETS=("/root/mlModel/web/Server.py")
for target in "${TARGETS[@]}"
do
      PID=$(ps aux | grep -v grep | grep $target | awk '{print $2}')
      echo $PID
      if [[ -z "$PID" ]]
      then
              echo "starting $target with nohup for env't: $ENVT"
              nohup python $target $ENVT $COMPONENTS &
      fi
done