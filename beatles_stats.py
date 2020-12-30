import numpy as np
import csv
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\Mateusz\\Documents\\The Beatles\\Beatles table")
rows = []
fields = []
filename = 'Beatles.csv'
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

beatles = np.array(rows)
y = list(range(2, 28, 2))
unique = []
lengths = []
liked = [[]] * 13
disliked = [[]] * 13
rliked = [[]] * 13
rdisliked = [[]] * 13
arrays = [[]] * 13
figs = [[]] * 13
pies = [[]] * 13
fl = [[]] * 13
fd = [[]] * 13
for x in range(13):
    unique.append(np.unique(beatles[:, y[x]]))
    unique[x] = list(unique[x])
    while ("" in unique[x]):
        unique[x].remove("")

for z in range(13):
    liked[z] = []
    disliked[z] = []
    for x in unique[z]:
        liked[z].append((len([elem for elem in beatles[:, y[z]] if elem == x])) / len(beatles))
        disliked[z].append((len([elem for elem in beatles[:, y[z] + 1] if elem == x])) / len(beatles))

for z in range(13):
    liked[z].insert(len(unique[z]) + 1, 1 - sum(liked[z]))
    disliked[z].insert(len(unique[z]) + 1, 1 - sum(disliked[z]))
    unique[z].insert(len(unique[z]) + 1, "Abstained")

for x in range(13):
    rliked[x] = []
    rdisliked[x] = []
    lengths.insert(x, len(unique[x]))
    for y in range(lengths[x]):
        rliked[x].append(round(liked[x][y], 5))
        rdisliked[x].append(round(disliked[x][y], 5))

for x in range(13):
    arrays[x] = np.array([unique[x], rliked[x], rdisliked[x]])
    figs[x] = go.Figure(data=[go.Table(header=dict(values=['Song names', 'Percentage liked', 'Percentage disliked']),
                                       cells=dict(values=[arrays[x][0], arrays[x][1], arrays[x][2]]))
                              ])

pies[0] = plt.pie(arrays[0][1, :], labels=unique[0], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[0])))  # FPPM
plt.pie(arrays[1][1, :], labels=unique[1], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[1])))  # FWTB
plt.pie(arrays[2][1, :], labels=unique[2], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[2])))  # FHDN
plt.pie(arrays[3][1, :], labels=unique[3], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[3])))  # FBFS
plt.pie(arrays[4][1, :], labels=unique[4], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[4])))  # FH
plt.pie(arrays[5][1, :], labels=unique[5], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[5])))  # FRS
plt.pie(arrays[6][1, :], labels=unique[6], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[6])))  # FR
plt.pie(arrays[7][1, :], labels=unique[7], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[7])))  # FSPL
plt.pie(arrays[8][1, :], labels=unique[8], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[8])))  # FMMT
plt.pie(arrays[9][1, :], labels=unique[9], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[9])))  # FWA
plt.pie(arrays[10][1, :], labels=unique[10], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[10])))  # FYS
plt.pie(arrays[11][1, :], labels=unique[11], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[11])))  # FLIB
plt.pie(arrays[12][1, :], labels=unique[12], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[12])))  # FAB

plt.pie(arrays[0][2, :], labels=unique[0], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[0])))  # LPMM
plt.pie(arrays[1][2, :], labels=unique[1], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[1])))  # LWTB
plt.pie(arrays[2][2, :], labels=unique[2], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[2])))  # LHDN
plt.pie(arrays[3][2, :], labels=unique[3], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[3])))  # LBFS
plt.pie(arrays[4][2, :], labels=unique[4], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[4])))  # LH
plt.pie(arrays[5][2, :], labels=unique[5], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[5])))  # LRS
plt.pie(arrays[6][2, :], labels=unique[6], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[6])))  # LR
plt.pie(arrays[7][2, :], labels=unique[7], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[7])))  # LSPL
plt.pie(arrays[8][2, :], labels=unique[8], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[8])))  # LMMT
plt.pie(arrays[9][2, :], labels=unique[9], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[9])))  # LWA
plt.pie(arrays[10][2, :], labels=unique[10], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[10])))  # LYS
plt.pie(arrays[11][2, :], labels=unique[11], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[11])))  # LLIB
plt.pie(arrays[12][2, :], labels=unique[12], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[12])))  # LAB

def print_lib(libname):
    name_1 = ['FPPM', 'FWTB', 'FHDN', 'FBFS', 'FH', 'FRS', 'FR', 'FSPL', 'FMMT', 'FWA', 'FYS', 'FLIB', 'FAB']
    name_2 = ['LPMM', 'LWTB', 'LHDN', 'LBFS', 'LH', 'LRS', 'LR', 'LSPL', 'LMMT', 'LWA', 'LYS', 'LLIB', 'LAB']

    if libname in name_1:
        i = name_1.index(libname)
        plt.pie(arrays[i][1,:], labels = unique[i], startangle = 140, autopct = '%1.1f%%', explode = (
                    [0.1] * len(unique[i])))

    elif libname in name_2:
        i = name_2.index(libname)
        plt.pie(arrays[i][2,:], labels = unique[i], startangle = 140, autopct = '%1.1f%%', explode = ([0.1] * len(unique[i])))
    else:
        print("Name Error!")

        print_lib("FWA")

#  PPM
PFPPM = plt.bar(unique[0], liked[0], color="blue", width=0.7)
PLPPM = plt.bar(unique[0], disliked[0], bottom=liked[0], width=0.7, color="orange")
plt.legend((PFPPM[0], PLPPM[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  WTB
PFWTB = plt.bar(unique[1], liked[1], color="blue", width=0.7)
PLWTB = plt.bar(unique[1], disliked[1], bottom=liked[1], width=0.7, color="orange")
plt.legend((PFWTB[0], PLWTB[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  HDN
PFHDN = plt.bar(unique[2], liked[2], color="blue", width=0.7)
PLHDN = plt.bar(unique[2], disliked[2], bottom=liked[2], width=0.7, color="orange")
plt.legend((PFHDN[0], PLHDN[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  BFS
PFBFS = plt.bar(unique[3], liked[3], color="blue", width=0.7)
PLBFS = plt.bar(unique[3], disliked[3], bottom=liked[3], width=0.7, color="orange")
plt.legend((PFBFS[0], PLBFS[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  H
PFH = plt.bar(unique[4], liked[4], color="blue", width=0.7)
PLH = plt.bar(unique[4], disliked[4], bottom=liked[4], width=0.7, color="orange")
plt.legend((PFH[0], PLH[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  RS
PFRS = plt.bar(unique[5], liked[5], color="blue", width=0.7)
PLRS = plt.bar(unique[5], disliked[5], bottom=liked[5], width=0.7, color="orange")
plt.legend((PFRS[0], PLRS[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  R
PFR = plt.bar(unique[6], liked[6], color="blue", width=0.7)
PLR = plt.bar(unique[6], disliked[6], bottom=liked[6], width=0.7, color="orange")
plt.legend((PFR[0], PLR[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  SPL
PFSPL = plt.bar(unique[7], liked[7], color="blue", width=0.7)
PLSPL = plt.bar(unique[7], disliked[7], bottom=liked[7], width=0.7, color="orange")
plt.legend((PFSPL[0], PLSPL[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  MMT
PFMMT = plt.bar(unique[8], liked[8], color="blue", width=0.7)
PLMMT = plt.bar(unique[8], disliked[8], bottom=liked[8], width=0.7, color="orange")
plt.legend((PFMMT[0], PLMMT[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  WA
PFWA = plt.bar(unique[9], liked[9], color="blue", width=0.7)
PLWA = plt.bar(unique[9], disliked[9], bottom=liked[9], width=0.7, color="orange")
plt.legend((PFWA[0], PLWA[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  YS
PFYS = plt.bar(unique[10], liked[10], color="blue", width=0.7)
PLYS = plt.bar(unique[10], disliked[10], bottom=liked[10], width=0.7, color="orange")
plt.legend((PLYS[0], PFYS[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  LIB
PFLIB = plt.bar(unique[11], liked[11], color="blue", width=0.7)
PLLIB = plt.bar(unique[11], disliked[11], bottom=liked[11], width=0.7, color="orange")
plt.legend((PFLIB[0], PLLIB[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)
#  AB
PFAB = plt.bar(unique[12], liked[12], color="blue", width=0.7)
PLAB = plt.bar(unique[12], disliked[12], bottom=liked[12], width=0.7, color="orange")
plt.legend((PFAB[0], PLAB[0]), ('Liked', 'Disliked'))
plt.xticks(rotation=20, size=6)

# Clearance
unique.clear()
lengths.clear()
liked.clear()
disliked.clear()
rliked.clear()
rdisliked.clear()
arrays.clear()
figs.clear()
