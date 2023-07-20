#!/bin/bash

path=${1:-"examples"}
shopt -s nullglob
find $path -type f -name '[!_]*.json' -print0 | while IFS= read -r -d '' json_file; do
    schema_file="schemas/locareCollection.schema.json"
    echo "Validating $json_file"
    ajv validate -c ajv-formats -s $schema_file -d $json_file -r schemas/locareAtlasMesh.schema.json -r schemas/locareCylinder.schema.json -r schemas/locareLineString.schema.json -r schemas/locarePoint.schema.json -r schemas/locarePolygon.schema.json -r schemas/locarePolyhedron.schema.json -r schemas/locareSphere.schema.json
    if [ $? -ne 0 ]; then
        echo "$json_file is not valid according to $schema_file"
        exit 1
    fi
done