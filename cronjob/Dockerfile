ARG COMMAND_VERSION=latest
FROM ghcr.io/daniele-athome/immich-carddav-sync:${COMMAND_VERSION} AS runtime

RUN apt-get update && apt-get install --no-install-recommends -y gettext-base cron

COPY crontab.tmpl /app/crontab.tmpl

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
