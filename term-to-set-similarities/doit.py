#!/bin/python3

import os
import re
import subprocess

total_output = '\tsimui\n'
total_output += 'term\tgold\tmedgen\tarup\tmayo\n'

terms = set()
for line in open('../set_instance_annots.tsv'):
    line = line.rstrip()
    cells = line.split('\t')
    if len(cells) == 1:
        continue
    terms |= set(cells[1].split(';'))

terms = sorted(list(terms))

annots_file = open('instance_annots.tsv', 'w')
annots_file.write(open('../set_instance_annots.tsv').read() + '\n')
for term in terms:
    annots_file.write(term.replace(':', '') + '\t' + term + '\n')
annots_file.close()

queries_file = open('input_queries.tsv', 'w')
for term in terms:
    term_id = term.replace(':', '')
    queries_file.write(term_id + '\tgold\n')
    queries_file.write(term_id + '\tmedgen\n')
    queries_file.write(term_id + '\tarup\n')
    queries_file.write(term_id + '\tmayo\n')
queries_file.close()

subprocess.call('java -jar ../slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml', shell=True)
output_file_contents = open('output.tsv').read()

for term in terms:
    term_id = term.replace(':', '')
    gold = re.compile(term_id + r'\tgold\t([0-9.]+)').search(output_file_contents)
    medgen = re.compile(term_id + r'\tmedgen\t([0-9.]+)').search(output_file_contents)
    arup = re.compile(term_id + r'\tarup\t([0-9.]+)').search(output_file_contents)
    mayo = re.compile(term_id + r'\tmayo\t([0-9.]+)').search(output_file_contents)
    if gold and medgen and arup and mayo:
        total_output += term + '\t' + gold.group(1) + '\t' + medgen.group(1) + '\t' + arup.group(1) + '\t' + mayo.group(1) + '\n'

os.remove('instance_annots.tsv')
os.remove('input_queries.tsv')
os.remove('output.tsv')
output_file = open('term-to-set-similarities.tsv', 'w')
output_file.write(total_output)
print(total_output)
