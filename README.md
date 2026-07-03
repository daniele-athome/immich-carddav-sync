Immich CardDAV sync tool
========================

A tool to sync dates of birth in Immich from a CardDAV server.

Configuration is provided via environment variables (`.env` file is supported).

| Name                             | Description                                    |
|----------------------------------|------------------------------------------------|
| CARDDAV_SYNC_CARDDAV_URL         | URL to the CardDAV server                      |
| CARDDAV_SYNC_CARDDAV_ADDRESSBOOK | Address book name or ID in the CardDAV server. |
| CARDDAV_SYNC_CARDDAV_USERNAME    | Username of CardDAV server                     |
| CARDDAV_SYNC_CARDDAV_PASSWORD    | Password of CardDAV server                     |
| CARDDAV_SYNC_IMMICH_API_URL      | Immich instance API URL (including "/api")     |
| CARDDAV_SYNC_IMMICH_API_KEY      | Immich API key                                 |
| CARDDAV_SYNC_CRON_EXPRESSION     | Cron expression (only for daemon image)        |

Environment variable LOG_LEVEL will configure the logging level (standard Python logging levels: DEBUG, INFO, WARNING,
ERROR, CRITICAL).

## Implementation notes

* matching between contacts and Immich people is between the Immich person's name and the following fields in the contact, **in this order**:
  * [formatted name](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.1)
  * [given name + family name](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2), separated by a space
  * [nickname](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.3)
* only the first matching contact will be used
* people in Immich with the same name will have the same date of birth

## Installation

Running the tool needs Poetry for now.

```shell
poetry install
poetry run immich-carddav-sync
```

## Usage with Docker

Add a cronjob in your system that executes this command:

```shell
docker run --rm --name immich-carddav-sync --env-file=immich-carddav-sync.env ghcr.io/daniele-athome/immich-carddav-sync:master
```

The `immich-carddav-sync.env` file should contain all the necessary environment variables (see above). If you prefer you
can add those variables to the Immich `.env` file itself and reference that one.

## Integrate in Immich (docker compose)

Configure the variables described above in your `.env` file and add a service to your `docker-compose.yml` file using
the daemon image:

```yaml
services:
  [...]

  carddav-sync:
    container_name: immich_carddav_sync
    image: ghcr.io/daniele-athome/immich-carddav-sync-daemon:latest
    env_file:
      - .env
    restart: always
    depends_on:
      - immich-server

  [...]
```

## Roadmap

* use s6-overlay instead of simple Debian cron (mainly because of vixie-cron not reacting to signals)
* support for duplicate contacts (ask interactively or assume a predefined behavior)
* match names with a custom (or multiple) vCard field(s)
* dry run mode
