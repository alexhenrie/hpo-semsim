#!/bin/python3

import os
import re
import subprocess
import sys

from hpo import hpo_terms

if len(sys.argv) == 1:
    print('Please specify the folder that has the input files.')
    exit(1)

os.chdir(sys.argv[1])

#parse the sets of terms
term_sets = dict()
term_sets['all'] = set()
for line in open('set_instance_annots.tsv'):
    line = line.rstrip()
    cells = line.split('\t')
    if len(cells) == 1:
        continue
    term_sets[cells[0]] = set(cells[1].split(';'))
    term_sets['all'] |= term_sets[cells[0]]


#sort the set of all terms
term_sets['all'] = sorted(list(term_sets['all']))

#define which sets will appear in the output (every one except the 'all' set)
set_names = list(term_sets.keys())
set_names.remove('all')

#write the header
total_output = '\t\tbest term-to-term simui'
for set_name in set_names:
    total_output += '\t'
total_output += 'best term-to-term simui0\nterm id\tterm name'
for set_name in set_names:
    total_output += '\t' + set_name
for set_name in set_names:
    total_output += '\t' + set_name
total_output += '\n'

#write an annotation file giving each term an ID
annots_file = open('instance_annots.tsv', 'w')
annots_file.write(open('set_instance_annots.tsv').read() + '\n')
for term in term_sets['all']:
    annots_file.write(term.replace(':', '') + '\t' + term + '\n')
annots_file.close()

#compare the terms
for term in term_sets['all']:
    simui_scores = dict()
    simui0_scores = dict()
    for set_name in set_names:
        if term in term_sets[set_name]:
            best_simui = 1
            best_simui0 = 1
        else:
            queries_file = open('input_queries.tsv', 'w')
            for set_term in term_sets[set_name]:
                queries_file.write(term.replace(':', '') + '\t' + set_term.replace(':', '') + '\n')
            queries_file.close()
            subprocess.call('java -jar ../../sml-toolkit-latest.jar -t sm -xmlconf ../sml-xmlconf-hpo.xml', shell=True)

            best_simui = 0;
            best_simui0 = 0;
            for match in re.finditer(r'\t([0-9.]+)\t([0-9.]+)', open('output.tsv').read()):
                score = float(match.group(1))
                if score > best_simui:
                    best_simui = score
                score = float(match.group(2))
                if score > best_simui0:
                    best_simui0 = score

        simui_scores[set_name] = best_simui
        simui0_scores[set_name] = best_simui0

    total_output += term + '\t' + hpo_terms[term]['name']
    for set_name in set_names:
        total_output += '\t' + str(simui_scores[set_name])
    for set_name in set_names:
        total_output += '\t' + str(simui0_scores[set_name])
    total_output += '\n'

#clean up
os.remove('instance_annots.tsv')
os.remove('input_queries.tsv')
os.remove('output.tsv')
output_file = open('term-to-set-similarities.tsv', 'w')
output_file.write(total_output)
print(total_output)
