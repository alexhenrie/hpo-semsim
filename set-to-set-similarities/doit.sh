#!/bin/sh

if [ $# -eq 0 ]; then
    echo "Please specify the folder that has the input files."
    exit 1
fi

cd $1
java -jar ../../sml-toolkit-latest.jar -t sm -xmlconf ../sml-xmlconf-hpo.xml
cat set-to-set-similarities.tsv
