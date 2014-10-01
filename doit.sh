#!/bin/sh
./data-to-annotations.py noonan_data.csv > instance_annots.tsv
echo "i1	i2" > input_queries.tsv
java -jar sml-toolkit-0.9.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat output.txt
