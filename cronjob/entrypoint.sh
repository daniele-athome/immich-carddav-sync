#!/bin/sh

env >> /etc/environment

export CRON_EXPRESSION="${CARDDAV_SYNC_CRON_EXPRESSION}"
envsubst < /app/crontab.tmpl >/etc/cron.d/immich-carddav-sync

exec cron -f
