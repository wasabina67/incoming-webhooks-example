#!/bin/bash

source .env

data=$(jq -n --arg text "text" '{"text": $text}')
curl -X POST -H "Content-Type: application/json" -d "$data" "$WEB_HOOKS_URL"
