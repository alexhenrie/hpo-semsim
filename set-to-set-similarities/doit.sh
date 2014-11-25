#!/bin/sh
java -jar ../slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat set-to-set-similarities.tsv
