#!/usr/bin/env bash
# Usage: ./experiments.sh https://url.to.immich/api api_key
# needs khard to be configured for contacts: https://khard.readthedocs.io/
# dependencies:
# - khard
# - jq
# - curl

BASE_URL="$1"
API_KEY="$2"

api_get() {
  curl -s -X GET --location -H "X-api-key: $API_KEY" "$BASE_URL/$1"
}

_api_body() {
  method="$1"
  shift
  curl -s -X "$method" --data-raw "$2" --location -H "content-type: application/json" -H "X-api-key: $API_KEY" "$BASE_URL/$1"
}

urlencode() {
  jq -rn --arg data "$1" '$data|@uri'
}

api_put() {
  _api_body "PUT" "$@"
}

cleanup() {
  [ -d "TMP_CONTACTS" ] && rm -fr "TMP_CONTACTS"
}

name_exact_matches() {
  awk -F'\t' '{print $2}' < "$TMP_CONTACTS" | grep -c "$1"
}

name_exact_match_line() {
  awk -F'\t' '{print $2}' < "$TMP_CONTACTS" | grep -xn "$1" | awk -F':' '{print $1}'
}

name_birth_date() {
  lineno="$(name_exact_match_line "$1")"
  [ -n "$lineno" ] && head -n "$lineno" < "$TMP_CONTACTS" | tail -1 | awk -F'\t' '{print $1}' | awk -F'.' '{print $1 "-" $2 "-" $3}'
}

trap cleanup EXIT

TMP_CONTACTS="$(mktemp)"

echo "Requesting all contacts..."
khard birthdays -d formatted_name -p >"$TMP_CONTACTS"

echo "Requesting all people..."
while read -r person; do

  person_id="$(echo "$person" | jq -r '.id')"
  person_name="$(echo "$person" | jq -r '.name')"
  if [[ -z "$person_name" ]]; then
    continue
  fi

  echo "$person_id ($person_name)"
  if [[ "$(name_exact_matches "$person_name")" -gt 1 ]]; then
    echo "More than one match for name. Aborting."
    exit 1
  fi

  birth_date=$(name_birth_date "$person_name")
  if [[ -n "$birth_date" ]]; then
    echo "Setting birth date for $person_name to $birth_date"
    api_put "person/$person_id" "$(jq -ncM --arg birthDate "$birth_date" '{"birthDate":$birthDate}')" >/dev/null
  fi

done < <(api_get person | jq -c '.people[]')
