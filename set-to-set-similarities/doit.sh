#!/bin/sh
java -jar ../sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat set-to-set-similarities.tsv
