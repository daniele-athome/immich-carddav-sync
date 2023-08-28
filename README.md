Immich CardDAV sync tool
========================

A tool to sync dates of birth in Immich from a CardDAV server.

Configuration is provided via environment variables (`.env` file is supported).

| Name                               | Description                                    |
|------------------------------------|------------------------------------------------|
| IMMICH_CARDDAV_CARDDAV_URL         | URL to the CardDAV server                      |
| IMMICH_CARDDAV_CARDDAV_ADDRESSBOOK | Address book name or ID in the CardDAV server. |
| IMMICH_CARDDAV_CARDDAV_USERNAME    | Username of CardDAV server                     |
| IMMICH_CARDDAV_CARDDAV_PASSWORD    | Password of CardDAV server                     |
| IMMICH_CARDDAV_IMMICH_API_URL      | Immich instance API URL (including "/api")     |
| IMMICH_CARDDAV_IMMICH_API_KEY      | Immich API key                                 |

Environment variable LOG_LEVEL will configure the logging level (standard Python logging levels: DEBUG, INFO, WARNING,
ERROR, CRITICAL).

## Implementation notes

* matching between contacts and Immich people is between
  the [full name field](https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.1) of the contact and the Immich
  person's name
* people in Immich with the same name will have the same date of birth
* duplicate contacts (i.e. with identical full name) are not supported yet (will cause exit with error)

## Installation

> TODO package install

Running the tool needs Poetry for now.

FIXME poetry preparation etc.

```shell
poetry run immich-carddav-sync
```

## Roadmap

* docker-compose.yml tutorial based on the one provided by the Immich project
* support for duplicate contacts (ask interactively or assume a predefined behavior)
* match names with a custom (or multiple) vCard field(s)
* dry run mode
