#!/bin/bash
# send a request to an URL using curl
curl -s "$1" | wc -c

