#!/bin/bash

set -e

TOOL_ROOT="../esp8266-sdk/tools"
ESP_TOOL="$TOOL_ROOT/esptool/esptool"
OTA_TOOL="$TOOL_ROOT/espota.py"

function usage()
{
    echo "Usage: $0 <FILE> serial <PORT> [BAUD]"
    echo "       $0 <FILE> ota <NAME> [PASS] [-p PORT]"
    exit 1
}

if [ "$#" -lt 1 ]; then
    usage
fi

FILE="build/$1.bin"
if [ ! -e "$FILE" ]; then
    usage
else
    shift
fi

echo "Uploading file: $FILE"

if [ "$1" == "serial" ]; then
    shift
    PORT="${1:-/dev/ttyUSB0}"
    BAUD="${2:-230400}"
    $ESP_TOOL -cd nodemcu -cp $PORT -cb $BAUD -ca 0x0000 -cf "$FILE"
elif [ "$1" == "ota" ]; then
    shift
    HOSTNAME="$1"

    if [[ -n "$(which jq)" && -f "upload_aliases.json" ]]; then
        MAYBE_HOSTNAME=$(jq --raw-output ".\"${HOSTNAME}\"" upload_aliases.json)
        if [[ "$MAYBE_HOSTNAME" != "null" ]]; then
            echo "$HOSTNAME is aliased to $MAYBE_HOSTNAME"
            HOSTNAME=$MAYBE_HOSTNAME
        fi
    fi

    ARGS=""
    [ -n "$2" ] && ARGS="$ARGS -a $2"
    if [ "$3" == "-p" ]; then
        ARGS="$ARGS -p $4"
    else
        ARGS="$ARGS -p 8266"
    fi
    #python3 $OTA_TOOL -d -i $(avahi-resolve-host-name -4 "${1}.local" | cut -f2) $ARGS -f "$FILE"
    #python3 $OTA_TOOL -d -i $(dig +short ${HOSTNAME})  $ARGS -f "$FILE"
    python3 $OTA_TOOL -d -i $HOSTNAME  $ARGS -f "$FILE"
else
    usage
fi
