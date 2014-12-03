#!/bin/python3
#compares all interesting terms to each set, returning the best SimUI score between the term and each of the terms in the set

import os
import re
import subprocess

#define which sets we care about
set_names = ['gold', 'top10', 'medgen', 'arup', 'mayo', 'hcm-concise', 'omim']

#write the header
total_output = '\tbest term-to-term simui\nterm'
for set_name in set_names:
    total_output += '\t' + set_name
total_output += '\n'

#parse the sets of terms
term_sets = dict()
term_sets['all'] = set()
for line in open('../set_instance_annots.tsv'):
    line = line.rstrip()
    cells = line.split('\t')
    if len(cells) == 1:
        continue
    term_sets[cells[0]] = set(cells[1].split(';'))
    term_sets['all'] |= term_sets[cells[0]]

#sort the set of all terms
term_sets['all'] = sorted(list(term_sets['all']))

#write an annotation file giving each term an ID
annots_file = open('instance_annots.tsv', 'w')
annots_file.write(open('../set_instance_annots.tsv').read() + '\n')
for term in term_sets['all']:
    annots_file.write(term.replace(':', '') + '\t' + term + '\n')
annots_file.close()

#compare the terms
for term in term_sets['all']:
    scores = dict()
    for set_name in set_names:
        queries_file = open('input_queries.tsv', 'w')
        for set_term in term_sets[set_name]:
            queries_file.write(term.replace(':', '') + '\t' + set_term.replace(':', '') + '\n')
        queries_file.close()
        subprocess.call('java -jar ../slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar -t sm -xmlconf sml-xmlconf-hpo.xml', shell=True)

        best_score = 0;
        for match in re.finditer(r'\t([0-9.]+)', open('output.tsv').read()):
            score = float(match.group(1))
            if score > best_score:
                best_score = score

        scores[set_name] = best_score

    total_output += term
    for set_name in set_names:
        total_output += '\t' + str(scores[set_name])
    total_output += '\n'

#clean up
os.remove('instance_annots.tsv')
os.remove('input_queries.tsv')
os.remove('output.tsv')
output_file = open('term-to-set-similarities.tsv', 'w')
output_file.write(total_output)
print(total_output)
