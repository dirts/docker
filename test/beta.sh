#!/bin/bash
# Start facebook service

if [[ $1 != '' ]]; then
    PORT=$1
else
    PORT=8222
fi

echo Will start wscg with port $PORT in dev cluster and debug log enabled
echo To ignore permission restriction, please run this script with env CG_IGNORE_PERMISSION_CONTROL=true
echo To avoid service register which will expose this service to dev cluster, please run this script with env CG_NO_REGISTER=true

for s in `ps -ef | grep uwsgi|grep $PORT| grep -v grep | awk '{print $2}'`;do kill -s 15 $s ;done
sleep 1
for s in `ps -ef | grep uwsgi|grep $PORT| grep -v grep | awk '{print $2}'`;do kill -s 9 $s ;done
sleep 1

uwsgi --http :$PORT --gevent 10 --processes 1 --module "mymodule:say" --harakiri 400 \
    --env "PAAS_SERVICE_PORTS=$PORT" \
    --env "PAAS_CLUSTER=beta" \
    --env "PAAS_LOG_LEVEL=DEBUG" \
    --env "PAAS_LOG_LEVEL=INFO" \
    --need-app \
    --lazy
