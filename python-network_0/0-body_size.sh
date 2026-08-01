#!/bin/bash
# Displays the size, in bytes, of the body of the response from a URL
curl -s -o /dev/null -w "%{size_download}\n" "$1"
