#!/usr/bin/env bash
set -u
/app.py $REGEX_ID
echo "Enter your expiry date (accepts up to $MAXCHARS characters)."
IFS= read ATTEMPT
if [ ${#ATTEMPT} -le $MAXCHARS ]; then
  export ATTEMPT
  time eval /app.py $REGEX_ID $REDOS_FLAG
else
  echo "Can only accept $MAXCHARS characters :("
fi
