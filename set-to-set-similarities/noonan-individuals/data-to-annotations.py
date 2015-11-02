#!/usr/bin/python3
#generates instance_annots.tsv and input_queries.tsv from noonan_data.csv

import csv

csvfile = open('noonan_data.csv', 'r')
reader = csv.reader(csvfile)
annots_file = open('instance_annots.tsv', 'w')
queries_file = open('input_queries.tsv', 'w')
i = -1
for row in reader:
    i += 1

    #skip first row
    if i == 0:
        continue

    phenotypes = []

    if row[2] == '1':
        phenotypes.append('HP:0000475') #broad neck
        phenotypes.append('HP:0000465') #webbed neck
    if row[3] == '1':
        phenotypes.append('HP:0000271') #abnormality of the face
    if row[4] == '1':
        phenotypes.append('HP:0001928') #abnormality of coagulation
    if row[5] == '1':
        phenotypes.append('HP:0000028') #cryptorchidism
    if row[6] == '1':
        phenotypes.append('HP:0000365') #hearing impairment
    if row[7] == '1':
        phenotypes.append('HP:0001263') #global developmental delay
    if row[8] == '1':
        phenotypes.append('HP:0001639') #hypertrophic cardiomyopathy
    if row[9] == '1':
        phenotypes.append('HP:0002562') #low-set nipples
    if row[10] == '1':
        phenotypes.append('HP:0001004') #lymphedema
    if row[11] == '1':
        phenotypes.append('HP:0011355') #localized skin lesion
    if row[12] == 'ptosis':
        phenotypes.append('HP:0000508') #ptosis
    if row[13] == ' aortic valve thickening':
        phenotypes.append('HP:0001646') #abnormality of the aortic valve
    if row[15] == '1':
        phenotypes.append('HP:0000766') #abnormality of the sternum
    if row[16] == '1':
        phenotypes.append('HP:0001642') #pulmonic stenosis
    if row[17] == '1':
        phenotypes.append('HP:0004322') #short stature

    annots_file.write('i' + str(i) + '\t' + ';'.join(phenotypes) + '\n')

#generate combinatorial list of comparisons to make
for j in range(1, i + 1):
    for k in range(j + 1, i + 1):
        queries_file.write('i' + str(j) + '\t' + 'i' + str(k) + '\n')
