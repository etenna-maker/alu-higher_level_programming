#!/bin/bash
# Sends a GET request with the required header and displays the response body
curl -s -L -H "X-HolbertonSchool-User-Id: 98" "$1"
