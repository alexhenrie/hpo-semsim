#!/bin/sh
#Compares ARUP's set of Noonan phenotypes to MEDGEN's set of Noonan phenotypes
java -jar ../sml-toolkit-0.9.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat output.tsv
