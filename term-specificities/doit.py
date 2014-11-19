#!/bin/python3

import os
import subprocess

total_output = 'e1\te2\trada\tkyogoku\teilbeck1\n'

for line in open('../set_instance_annots.tsv'):
    line = line.rstrip()
    cells = line.split('\t')
    if len(cells) == 1:
        continue
    terms = cells[1].split(';')

    annots_file = open('instance_annots.tsv', 'w')
    annots_file.write('root\tHP:0000001\n')
    for term in terms:
        annots_file.write(term.replace(':', '') + '\t' + term + '\n')
    annots_file.close()

    queries_file = open('input_queries.tsv', 'w')
    for term in terms:
        queries_file.write('root\t' + term.replace(':', '') + '\n')
    queries_file.close()

    subprocess.call('java -jar ../slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml', shell=True)
    output_file_contents = open('output.tsv').read()
    total_output += cells[0] + '\n'
    total_output += output_file_contents[output_file_contents.index('\n') + 1:]

os.remove('instance_annots.tsv')
os.remove('input_queries.tsv')
os.remove('output.tsv')
output_file = open('term-specificities.tsv', 'w')
output_file.write(total_output)
print(total_output)
