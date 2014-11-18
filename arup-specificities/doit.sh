#!/bin/sh
#Computes 1 over the average distance to the root node as a way to measure specificity
java -jar ../slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat output.tsv
