#!/bin/sh

./data-to-annotations.py noonan_data.csv > instance_annots.tsv

#generate combinatorial list of comparisons to make
instance_count=`grep -c ^ instance_annots.tsv`
cp /dev/null input_queries.tsv
for i in `seq 1 $instance_count`; do
    for j in `seq $(($i+1)) $instance_count`; do
        echo "i$i	i$j" >> input_queries.tsv
    done
done

java -jar sml-toolkit-0.9.jar -t sm -xmlconf sml-xmlconf-hpo.xml
cat output.tsv
