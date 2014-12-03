#!/bin/python3

import os
import re

hpo_terms = dict()
term = None

for line in open(os.path.dirname(__file__) + '/hp.obo'):
    if line == '[Term]\n':
        term = dict()
        continue
    elif line == '\n' and term:
        term_id = term['id']
        del term['id']
        hpo_terms[term_id] = term
        term = None
        continue
    
    if term != None:
        tokens = re.search('(.*?): (.*)', line)
        if tokens.group(1) in ['id','name','def']:
            term[tokens.group(1)] = tokens.group(2)
