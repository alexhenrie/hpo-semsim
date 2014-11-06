#!/bin/sh
#Computes 1 over the average distance to the root node as a way to measure specificity
java -jar ../sml-toolkit-0.9.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat output.tsv
