#!/usr/bin/env bash
# TODO move this to Poetry

set -e
rm -fr temp
mkdir -p temp
curl "https://raw.githubusercontent.com/immich-app/immich/v1.91.4/server/immich-openapi-specs.json" >immich-openapi-specs.json
cd temp

python3 -m venv venv
source venv/bin/activate
pip install openapi-python-client
openapi-python-client generate --path ../immich-openapi-specs.json
cd -

rm -fr immich_carddav_sync/immich_client
cp -r temp/immich-client/immich_client immich_carddav_sync/
rm -fr temp
