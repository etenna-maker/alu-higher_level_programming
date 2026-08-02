#!/bin/bash
# Displays the response body only when the final HTTP status code is 200
[ "$(curl -s -L -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s -L "$1"
