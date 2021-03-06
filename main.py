import numpy as np
import csv

import plotly.graph_objects as go

import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd

#################################### Data Preparation #################################################
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
lsongs = []
alikes = list()
adislikes = list()
dfb = np.array("1")
wp = {'linewidth': 1, 'edgecolor': "black"}
font = {'family': 'serif',
        'color': 'darkred',
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
        dfb = np.vstack([dfb, unique[x][y]])
dfb = np.delete(dfb, (0))
for x in range(13):
    for y in range(len(unique[x])):
        alikes.append(likes[x][y])
        adislikes.append(dislikes[x][y])

dfb = np.c_[dfb, alikes]
dfb = np.c_[dfb, adislikes]

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


#################################### Methods #################################################

def button_logic():
    album = int(album_choice.get())
    which_plot = int(def_choose.get())

    di = {0: 'AB', 1: 'BFS', 2: 'H', 3: 'HDN', 4: 'LIB', 5: 'MMT', 6: 'PPM', 7: 'R', 8: 'RS', 9: 'SPL', 10: 'WA',
          11: 'WTB', 12: 'YS'}

    if which_plot == 1:  # Most Liked
        ciastko(f"F{di[album]}")
    elif which_plot == 2:  # Most Disliked
        ciastko(f"L{di[album]}")
    else:  # Barchart
        bar(di[album])

def ciastko(libname):
    name_1 = ['FPPM', 'FWTB', 'FHDN', 'FBFS', 'FH', 'FRS', 'FR', 'FSPL', 'FMMT', 'FWA', 'FYS', 'FLIB', 'FAB']
    name_2 = ['LPPM', 'LWTB', 'LHDN', 'LBFS', 'LH', 'LRS', 'LR', 'LSPL', 'LMMT', 'LWA', 'LYS', 'LLIB', 'LAB']

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

    matplotlib.use("TkAgg")
    fig = Figure(figsize=(5, 4))
    plot = fig.add_subplot(1, 1, 1)

    if libname in name_1:

        fig3, ax3 = plt.subplots()
        i = name_1.index(libname)
        ax3.pie(arrays[i][1, :], explode=([0.1] * len(unique[i])), labels=unique[i], autopct='%1.1f%%',
               shadow="TRUE", startangle=140, wedgeprops=wp)
        plt.title(titles[title_short], titlefont)


    elif libname in name_2:

        fig3, ax3 = plt.subplots()
        i = name_2.index(libname)
        ax3.pie(arrays[i][2, :], labels=unique[i], startangle=140, autopct='%1.1f%%',
                        explode=([0.1] * len(unique[i])), wedgeprops=wp, shadow="TRUE")
        plt.title(titles[title_short], titlefont)

    else:
        print("Name Error!")

    canvas = FigureCanvasTkAgg(fig3, gui)
    canvas.get_tk_widget().grid(row=2, rowspan=len(titles), columnspan=3, column=1)
    tk.mainloop()



def bar(s):
    matplotlib.use("TkAgg")
    fig = Figure(figsize=(5, 4))
    plot = fig.add_subplot(1, 1, 1)

    libname = s

    # liked, disliked, unique, arrays, wp, titlefont, font = plot_prepare()
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
    PL = ax.bar(unique_sorted, disliked_sorted, bottom=liked_sorted, width=0.7, edgecolor="black",
                color="#ff445f", )
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

    canvas = FigureCanvasTkAgg(fig, gui)
    canvas.get_tk_widget().grid(row=2, rowspan=len(titles), columnspan=3, column=1)

    tk.mainloop()

#################################### GUI #################################################
matplotlib.use("TkAgg")

gui = tk.Tk()
gui.title("Beatles Statistics")

titles = {'AB': "Abbey Road", 'BFS': "Beatles For Sale", 'H': "Help!", 'HDN': "A Hard Day's Night", 'LIB': "Let It Be",
          'MMT': "Magical Mystery Tour", 'PPM': "Please Please Me", 'R': "Revolver", 'RS': "Rubber Soul",
          'SPL': "Sgt. Pepper's Lonely Hearts Club Band", 'WA': "The White Album", 'WTB': "With The Beatles",
          'YS': "Yellow Submarine"}

i = 0
album_choice = tk.StringVar()
for r in titles:
    tk.Radiobutton(text=titles[r], borderwidth=1, width=40, value=i, variable=album_choice).grid(row=i + 2, column=0)
    i += 1

btn = tk.Button(gui, text="Show plot!", width=30, command=button_logic).grid(row=1, columnspan=3, column=1)

def_choose = tk.StringVar()
tk.Radiobutton(gui, text="Most Liked", borderwidth=1, width=15, value=1, variable=def_choose).grid(row=0, column=1)
tk.Radiobutton(gui, text="Most Disliked", borderwidth=1, width=15, value=2, variable=def_choose).grid(row=0, column=2)
tk.Radiobutton(gui, text="Bar Chart", borderwidth=1, width=15, value=3, variable=def_choose).grid(row=0, column=3)


figure = Figure(figsize=(5, 4))
plot = figure.add_subplot(1, 1, 1)

canvas = FigureCanvasTkAgg(figure, gui)
canvas.get_tk_widget().grid(row=2, rowspan=len(titles), columnspan=3, column=1)
tk.mainloop()