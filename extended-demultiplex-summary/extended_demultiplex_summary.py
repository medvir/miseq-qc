#!/usr/bin/env python3

import csv

# Creating dictionaries of index primers
I7_Index = {
    "TAAGGCGA": "N701", "CGTACTAG": "N702", "AGGCAGAA": "N703",
    "TCCTGAGC": "N704", "GGACTCCT": "N705", "TAGGCATG": "N706",
    "CTCTCTAC": "N707", "CAGAGAGG": "N708", "GCTACGCT": "N709",
    "CGAGGCTG": "N710", "AAGAGGCA": "N711", "GTAGAGGA": "N712"
    }

I5_Index = {
    "GCGTAAGA": "S517", "CTCTCTAT": "S502", "TATCCTCT": "S503",
    "AGAGTAGA": "S504", "GTAAGGAG": "S505", "ACTGCATA": "S506",
    "AAGGAGTA": "S507", "CTAAGCCT": "S508"
    }

Index_count = {}

txt_file = "170728_DemultiplexSummaryF1L1.txt"
csv_extended_file = "170728_DemultiplexSummaryF1L1Extended.csv"

out_csv = csv.writer(open(csv_extended_file, "w"))


def hamming_distance(I_sequenced, I_reference):
    assert len(I_sequenced) == len(I_reference)
    return sum(c1 != c2 for c1, c2 in zip(I_sequenced, I_reference))


try:
    in_txt = csv.reader(open(txt_file, "r"), delimiter="\t")
except OSError as e:
    print(e)

out_csv.writerow(["I7_fw", "I7_count", "I7_name"])

data = [row for row in in_txt]
# insert assertion to check if nothing was modidied
index1 = data[44:144]

for row in index1:
    I7_fw = str(row[0])
    I7_rv = str(row[1])
    I7_count = int(row[2])

    I7_name = ""
    if I7_fw in I7_Index.keys():
        I7_name = I7_Index[I7_fw]
        if I7_name in Index_count.keys():
            Index_count[I7_name] = Index_count[I7_name] + I7_count
        else:
            Index_count[I7_name] = I7_count

    for key in I7_Index:
        if hamming_distance(I7_fw, key) == 1:
            I7_name = I7_Index[key] + "*"
            Index_count[I7_Index[key]] = Index_count[I7_Index[key]] + I7_count

    out_csv.writerow([I7_fw, I7_count, I7_name])

out_csv.writerow(["I5_fw", "I5_count", "I5_name"])

# insert assertion to check if nothing was modidied
index2 = data[145:245]

for row in index2:
    I5_fw = str(row[0])
    I5_rv = str(row[1])
    I5_count = int(row[2])

    I5_name = ""
    if I5_fw in I5_Index.keys():
        I5_name = I5_Index[I5_fw]
        if I5_name in Index_count.keys():
            Index_count[I5_name] = Index_count[I5_name] + I5_count
        else:
            Index_count[I5_name] = I5_count

    for key in I5_Index:
        if hamming_distance(I5_fw, key) == 1:
            I5_name = I5_Index[key] + "*"
            Index_count[I5_Index[key]] = Index_count[I5_Index[key]] + I5_count

    out_csv.writerow([I5_fw, I5_count, I5_name])

print(Index_count)
