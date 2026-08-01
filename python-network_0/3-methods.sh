#!/bin/bash
# Displays all HTTP methods accepted by the server for a URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
