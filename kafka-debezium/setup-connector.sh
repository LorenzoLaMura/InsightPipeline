#!/bin/bash

# Replace environment variables in the config file
envsubst < /mysql-connector-config.json > /tmp/mysql-connector-config.json

# Create the connector using the processed config file
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors --data @/tmp/mysql-connector-config.json

# Keep the container running
tail -f /dev/null