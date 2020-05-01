#!/bin/bash

REQURIEMENTS=$(pip3 list --disable-pip3-version-check | grep -E newrelic-api | cut -d ' ' -f 1)
if [[ -z $REQURIEMENTS ]]; then
    echo "### Installing requirements ..."
    pip3 install git+git://github.com/ambitioninc/newrelic-api.git
fi

function usage(){
    echo '-h or --help | Help information
-k or --key | New Relic API Key
-s or --save | Save output to local
-i or --api | Choice an Rest API (applications, dashboards, users etc.)
-f or --function | Choice an function (list, show, backup etc.)
--format | Support Json and Yaml default is Json
--filter | Apply filter ex: --filter title="SRE" (default: all)
-r or --restore | Give a backup file path to restore'
}

FUNCTION=""
API=""
FORMAT="yaml"
SAVE=False
FILTER="all"
RESTORE=None

while [[ "$1" == -* ]]; do
  case "$1" in
  -h | --help)
    usage
    exit 0
    ;;
  -k | --key)
    shift
    export NEW_RELIC_API_KEY=$1
    ;;
  -s | --save)
    SAVE=True
    ;;
  -i | --api)
    shift
    API=$1
    ;;
  -f | --function)
    shift
    FUNCTION=$1
    ;;
  --filter)
    shift
    FILTER=$1
    ;;
  --format)
    shift
    FORMAT=$1
    ;;
  -r | --restore)
    shift
    RESTORE=$1
    ;;
  --)
    shift
    break
    ;;
  esac
  shift
done

echo "- API: ${API}"
echo "- Function: ${FUNCTION}"
echo "- Format: ${FORMAT}"
echo "- Save to local: ${SAVE}"
echo "- Apply filters: ${FILTER}"

if [[ ${FUNCTION} == "restore" ]] && [[ ${RESTORE} == None ]] ; then
    echo "Please set restore file name ex. -r backup-dashboard-ts.json"
    exit 1
elif [[ ${FUNCTION} == "restore" ]]; then    
    echo "Restore: ${RESTORE}"
fi

[[ -d output/${API} ]] || mkdir -p output/${API} 

python3 main.py ${API} ${FUNCTION} ${FORMAT} ${SAVE} "${FILTER}" ${RESTORE}