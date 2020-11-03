#!/usr/bin/env python

import csv

biosample_obi_map = {}
file_obi_map = {}

with open('biosample_obi_terms.txt') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter=' ')
    for row in reader:
        biosample_obi_map[row['sample']] = row['obi']

with open('file_describes_biosample.tsv') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    for row in reader:
        file_obi_map[row['file_local_id']] = biosample_obi_map[row['biosample_local_id']]

with open('file.tsv') as tsvfile,\
    open('file_with_assay.tsv', 'w') as file_assay_file:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    writer = csv.DictWriter(file_assay_file, fieldnames=reader.fieldnames, delimiter='\t')
    writer.writeheader()
    for row in reader:
        obi = None
        try:
            obi = file_obi_map[row['local_id']]
        except:
            pass
        row['assay_type'] = obi
        writer.writerow(row)
