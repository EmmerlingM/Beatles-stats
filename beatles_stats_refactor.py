import numpy as np
import csv
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
from collections import Counter


def csv_formating():
    beatles_csv = 'src/Beatles.csv'

    beatles_full = pd.read_csv(beatles_csv)
    naglowki = pd.read_csv(beatles_csv).columns.tolist()[2:28]

    discography = {}
    for columns in naglowki:
        song_title, votes = zip(*Counter((beatles_full[columns].tolist())).items())

        discography[str(columns)] = dict(zip(song_title, votes))

    return discography


def discograpgy2df(albumname):
    discpgraphy = csv_formating()
    liked_list = []
    disliked_list = []
    for key in discpgraphy[f"F{albumname}"]:
        
    print(discpgraphy[f"L{albumname}"])


    # df = pd.DataFrame({"Liked": liked[i],
    #                    "Disliked": disliked[i],
    #                    "Title": unique[i]
    #                    })
discograpgy2df("YS")

def bary(album_name):  # All possible album_name values: AB BFS H HDN LIB MMT PPM R RS SPL WA WTB YS
    discography = csv_formating()

    liked = discography[f"L{album_name}"]
    disliked = discography[f"F{album_name}"]

    print(liked)

    name_1 = ['AB', 'BFS', 'H', 'HDN', 'LIB', 'MMT', 'PPM', 'R', 'RS', 'SPL', 'WA', 'WTB', 'YS']
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

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
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
    plt.title(titles[album_name])
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
    plt.show()


