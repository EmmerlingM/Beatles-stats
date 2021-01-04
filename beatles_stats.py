import numpy as np
import csv
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd

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
keys = pd.read_csv("songs_data.csv")
y = list(range(2, 28, 2))
unique = []
lengths = []
liked = [[]] * 13
disliked = [[]] * 13
likes = [[]] * 13
dislikes = [[]] * 13
rliked = [[]] * 13
rdisliked = [[]] * 13
arrays = [[]] * 13
figs = [[]] * 13
songs = [[]] * 189
alikes = list()
adislikes = list()
df = np.array("1")
wp = {'linewidth': 1, 'edgecolor': "black"}
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
titlefont = {'family': 'serif',
             'color': 'black',
             'fontweight': 'bold',
             'size': 20}
for x in range(13):
    unique.append(np.unique(beatles[:, y[x]]))
    unique[x] = list(unique[x])
    while ("" in unique[x]):
        unique[x].remove("")

for z in range(13):
    liked[z] = []
    likes[z] = []
    disliked[z] = []
    dislikes[z] = []
    for x in unique[z]:
        liked[z].append((len([elem for elem in beatles[:, y[z]] if elem == x])) / len(beatles))
        likes[z].append(len([elem for elem in beatles[:, y[z]] if elem == x]))
        disliked[z].append((len([elem for elem in beatles[:, y[z] + 1] if elem == x])) / len(beatles))
        dislikes[z].append(len([elem for elem in beatles[:, y[z] + 1] if elem == x]))

for x in range(13):
    for y in range(len(unique[x])):
        df = np.vstack([df, unique[x][y]])
df = np.delete(df, (0))
for x in range(13):
    for y in range(len(unique[x])):
        alikes.append(likes[x][y])
        adislikes.append(dislikes[x][y])

df = np.c_[df, alikes]
df = np.c_[df, adislikes]

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

def ciastko(libname):
    name_1 = ['FPPM', 'FWTB', 'FHDN', 'FBFS', 'FH', 'FRS', 'FR', 'FSPL', 'FMMT', 'FWA', 'FYS', 'FLIB', 'FAB']
    name_2 = ['LPMM', 'LWTB', 'LHDN', 'LBFS', 'LH', 'LRS', 'LR', 'LSPL', 'LMMT', 'LWA', 'LYS', 'LLIB', 'LAB']

    title_short = libname[1:]

    titles = {
        'PPM': "Please Please Me",
        'WTB': "With The Beatles",
        'HDN': "A Hard Day's Night",
        'BFS': "Beatles For Sale",
        'H': "Help!",
        'RS': "Rubber Soul",
        'R': "Revolver",
        'SPL': "Sgt. Pepper's Lonely Hearts Club Band",
        'MMT': "Magical Mystery Tour",
        'WA': "The White Album",
        'YS': "Yellow Submarine",
        'LIB': "Let It Be",
        'AB': "Abbey Road",
    }

    if libname in name_1:
        i = name_1.index(libname)
        plt.pie(arrays[i][1, :], labels=unique[i], startangle=140, autopct='%1.1f%%', explode=(
                [0.1] * len(unique[i])), wedgeprops=wp, shadow="TRUE")
        plt.title(titles[title_short], titlefont)


    elif libname in name_2:
        i = name_2.index(libname)
        plt.pie(arrays[i][2, :], labels=unique[i], startangle=140, autopct='%1.1f%%',
                explode=([0.1] * len(unique[i])), wedgeprops=wp, shadow="TRUE")
        plt.title(titles[title_short], titlefont)

    else:
        print("Name Error!")

ciastko("LWA") #  You just input a name of the album from object "fields" which you would like to see


def bary(libname):
    name_1 = ['PPM', 'WTB', 'HDN', 'BFS', 'H', 'RS', 'R', 'SPL', 'MMT', 'WA', 'YS', 'LIB', 'AB']
    titles = {
        'PPM': "Please Please Me",
        'WTB': "With The Beatles",
        'HDN': "A Hard Day's Night",
        'BFS': "Beatles For Sale",
        'H': "Help!",
        'RS': "Rubber Soul",
        'R': "Revolver",
        'SPL': "Sgt. Pepper's Lonely Hearts Club Band",
        'MMT': "Magical Mystery Tour",
        'WA': "The White Album",
        'YS': "Yellow Submarine",
        'LIB': "Let It Be",
        'AB': "Abbey Road",
    }
    i = name_1.index(libname)

    df = pd.DataFrame({"Liked": liked[i],
                           "Disliked": disliked[i],
                           "Unique": unique[i]
                           })

    df_sorted = df.sort_values('Liked')
    unique_sorted = df_sorted["Unique"].tolist()
    disliked_sorted = df_sorted["Disliked"].tolist()
    liked_sorted = df_sorted["Liked"].tolist()

    top = max(liked_sorted)
    fig, ax = plt.subplots()
    PF = ax.bar(unique_sorted, liked_sorted, color="#11aabb", width=0.7, edgecolor="black")
    PL = ax.bar(unique_sorted, disliked_sorted, bottom=liked_sorted, width=0.7, edgecolor="black", color="#ff445f", )
    ax.text(s=unique[i][liked[i].index(top)], x=(len(liked[i]) / 2), y=(top / 2), size=50, alpha=0.2,
            horizontalalignment='center', verticalalignment='center', fontdict=font)
    ax.legend((PF[0], PL[0]), ('Liked', 'Disliked'), fontsize="xx-large", shadow=True)
    ax.set_axisbelow(True)
    ax.grid(b=True, which='both', axis='both', color='black', linewidth=0.7, alpha=0.2)
    plt.xticks(rotation=20, size=7)
    plt.ylabel("Percentage of votes", size=15, labelpad=20)
    plt.xlabel("Titles of the songs", size=15)
    plt.title(titles[libname], titlefont)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
bary("YS") #  You just input a name of the album from object "fields" which you would like to see

plt.show()

# for i in range(189):
#     for a in range(125):
#         songs[i].append(sum(df[i:,0] == keys.iloc[a,0]))

# Clearance
unique.clear()
lengths.clear()
liked.clear()
likes.clear()
alikes.clear()
disliked.clear()
dislikes.clear()
adislikes.clear()
rliked.clear()
rdisliked.clear()
arrays.clear()
figs.clear()
