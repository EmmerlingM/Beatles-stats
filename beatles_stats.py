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
wp = {'linewidth': 1, 'edgecolor': "black"}
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

plt.pie(arrays[0][1, :], labels=unique[0], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[0])),
        wedgeprops=wp, shadow="TRUE")  # FPPM
plt.pie(arrays[1][1, :], labels=unique[1], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[1])),
        wedgeprops=wp, shadow="TRUE")  # FWTB
plt.pie(arrays[2][1, :], labels=unique[2], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[2])),
        wedgeprops=wp, shadow="TRUE")  # FHDN
plt.pie(arrays[3][1, :], labels=unique[3], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[3])),
        wedgeprops=wp, shadow="TRUE")  # FBFS
plt.pie(arrays[4][1, :], labels=unique[4], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[4])),
        wedgeprops=wp, shadow="TRUE")  # FH
plt.pie(arrays[5][1, :], labels=unique[5], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[5])),
        wedgeprops=wp, shadow="TRUE")  # FRS
plt.pie(arrays[6][1, :], labels=unique[6], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[6])),
        wedgeprops=wp, shadow="TRUE")  # FR
plt.pie(arrays[7][1, :], labels=unique[7], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[7])),
        wedgeprops=wp, shadow="TRUE")  # FSPL
plt.pie(arrays[8][1, :], labels=unique[8], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[8])),
        wedgeprops=wp, shadow="TRUE")  # FMMT
plt.pie(arrays[9][1, :], labels=unique[9], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[9])),
        wedgeprops=wp, shadow="TRUE")  # FWA
plt.pie(arrays[10][1, :], labels=unique[10], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[10])), wedgeprops=wp, shadow="TRUE")  # FYS
plt.pie(arrays[11][1, :], labels=unique[11], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[11])), wedgeprops=wp, shadow="TRUE")  # FLIB
plt.pie(arrays[12][1, :], labels=unique[12], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[12])), wedgeprops=wp, shadow="TRUE")  # FAB

plt.pie(arrays[0][2, :], labels=unique[0], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[0])),
        wedgeprops=wp, shadow="TRUE")  # LPMM
plt.pie(arrays[1][2, :], labels=unique[1], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[1])),
        wedgeprops=wp, shadow="TRUE")  # LWTB
plt.pie(arrays[2][2, :], labels=unique[2], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[2])),
        wedgeprops=wp, shadow="TRUE")  # LHDN
plt.pie(arrays[3][2, :], labels=unique[3], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[3])),
        wedgeprops=wp, shadow="TRUE")  # LBFS
plt.pie(arrays[4][2, :], labels=unique[4], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[4])),
        wedgeprops=wp, shadow="TRUE")  # LH
plt.pie(arrays[5][2, :], labels=unique[5], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[5])),
        wedgeprops=wp, shadow="TRUE")  # LRS
plt.pie(arrays[6][2, :], labels=unique[6], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[6])),
        wedgeprops=wp, shadow="TRUE")  # LR
plt.pie(arrays[7][2, :], labels=unique[7], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[7])),
        wedgeprops=wp, shadow="TRUE")  # LSPL
plt.pie(arrays[8][2, :], labels=unique[8], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[8])),
        wedgeprops=wp, shadow="TRUE")  # LMMT
plt.pie(arrays[9][2, :], labels=unique[9], startangle=140, autopct='%1.1f%%', explode=([0.1] * len(unique[9])),
        wedgeprops=wp, shadow="TRUE")  # LWA
plt.pie(arrays[10][2, :], labels=unique[10], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[10])), wedgeprops=wp, shadow="TRUE")  # LYS
plt.pie(arrays[11][2, :], labels=unique[11], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[11])), wedgeprops=wp, shadow="TRUE")  # LLIB
plt.pie(arrays[12][2, :], labels=unique[12], startangle=140, autopct='%1.1f%%',
        explode=([0.1] * len(unique[12])), wedgeprops=wp, shadow="TRUE")  # LAB

#  def print_lib(libname):
#      name_1 = ['FPPM', 'FWTB', 'FHDN', 'FBFS', 'FH', 'FRS', 'FR', 'FSPL', 'FMMT', 'FWA', 'FYS', 'FLIB', 'FAB']
#      name_2 = ['LPMM', 'LWTB', 'LHDN', 'LBFS', 'LH', 'LRS', 'LR', 'LSPL', 'LMMT', 'LWA', 'LYS', 'LLIB', 'LAB']
#
#      if libname in name_1:
#          i = name_1.index(libname)
#          plt.pie(arrays[i][1,:], labels = unique[i], startangle = 140, autopct = '%1.1f%%', explode = (
#                      [0.1] * len(unique[i])), wedgeprops=wp, shadow="TRUE")
#
#      elif libname in name_2:
#          i = name_2.index(libname)
#          plt.pie(arrays[i][2,:], labels = unique[i], startangle = 140, autopct = '%1.1f%%',
#          explode = ([0.1] * len(unique[i])), wedgeprops=wp, shadow="TRUE")
#      else:
#          print("Name Error!")
#
#          print_lib("FWA") #  You just input a name of the album from object "fields" which you would like to see

#  PPM
PFPPM = plt.bar(unique[0], liked[0], color="#11aabb", width=0.7, edgecolor="black")
PLPPM = plt.bar(unique[0], disliked[0], bottom=liked[0], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFPPM[0], PLPPM[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  WTB
PFWTB = plt.bar(unique[1], liked[1], color="#11aabb", width=0.7, edgecolor="black")
PLWTB = plt.bar(unique[1], disliked[1], bottom=liked[1], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFWTB[0], PLWTB[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  HDN
PFHDN = plt.bar(unique[2], liked[2], color="#11aabb", width=0.7, edgecolor="black")
PLHDN = plt.bar(unique[2], disliked[2], bottom=liked[2], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFHDN[0], PLHDN[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  BFS
PFBFS = plt.bar(unique[3], liked[3], color="#11aabb", width=0.7, edgecolor="black")
PLBFS = plt.bar(unique[3], disliked[3], bottom=liked[3], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFBFS[0], PLBFS[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  H
PFH = plt.bar(unique[4], liked[4], color="#11aabb", width=0.7, edgecolor="black")
PLH = plt.bar(unique[4], disliked[4], bottom=liked[4], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFH[0], PLH[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  RS
PFRS = plt.bar(unique[5], liked[5], color="#11aabb", width=0.7, edgecolor="black")
PLRS = plt.bar(unique[5], disliked[5], bottom=liked[5], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFRS[0], PLRS[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  R
PFR = plt.bar(unique[6], liked[6], color="#11aabb", width=0.7, edgecolor="black")
PLR = plt.bar(unique[6], disliked[6], bottom=liked[6], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFR[0], PLR[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  SPL
PFSPL = plt.bar(unique[7], liked[7], color="#11aabb", width=0.7, edgecolor="black")
PLSPL = plt.bar(unique[7], disliked[7], bottom=liked[7], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFSPL[0], PLSPL[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  MMT
PFMMT = plt.bar(unique[8], liked[8], color="#11aabb", width=0.7, edgecolor="black")
PLMMT = plt.bar(unique[8], disliked[8], bottom=liked[8], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFMMT[0], PLMMT[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  WA
PFWA = plt.bar(unique[9], liked[9], color="#11aabb", width=0.7, edgecolor="black")
PLWA = plt.bar(unique[9], disliked[9], bottom=liked[9], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFWA[0], PLWA[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  YS
PFYS = plt.bar(unique[10], liked[10], color="#11aabb", width=0.7, edgecolor="black")
PLYS = plt.bar(unique[10], disliked[10], bottom=liked[10], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PLYS[0], PFYS[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  LIB
PFLIB = plt.bar(unique[11], liked[11], color="#11aabb", width=0.7, edgecolor="black")
PLLIB = plt.bar(unique[11], disliked[11], bottom=liked[11], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFLIB[0], PLLIB[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=7)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#  AB
PFAB = plt.bar(unique[12], liked[12], color="#11aabb", width=0.7, edgecolor="black")
PLAB = plt.bar(unique[12], disliked[12], bottom=liked[12], width=0.7, edgecolor="black", color="#ff445f")
plt.legend((PFAB[0], PLAB[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
plt.xticks(rotation=20, size=5.5)
plt.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
plt.axes().set_axisbelow(True)
#plt.text(text=f"{liked[12]==[(max(liked[12]))]}") #  TODO

# Clearance
unique.clear()
lengths.clear()
liked.clear()
disliked.clear()
rliked.clear()
rdisliked.clear()
arrays.clear()
figs.clear()
