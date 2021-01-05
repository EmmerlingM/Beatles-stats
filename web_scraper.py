from bs4 import BeautifulSoup
import requests
import csv


def csv_from_inwhatkey():
    csv_file = open('songs_data1.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', 'key'])

    source = requests.get('https://inwhatkey.com/artist/74-the-beatles').text
    soup = BeautifulSoup(source, 'lxml')

    domain_name = 'https://inwhatkey.com'

    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/song'):
            link = domain_name + a['href']
            current_source = requests.get(link).text
            current_soup = BeautifulSoup(current_source, 'lxml')

            key = current_soup.find("h3").text
            title = current_soup.find("h1").text
            csv_writer.writerow([title, key])

    csv_file.close()


def csv_from_SongKeyFinder():
    csv_file = open('songs_data2.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', 'key'])

    pages = [
        "https://www.songkeyfinder.com/search?page=1&artist=The%20Beatles&song=",
        "https://www.songkeyfinder.com/search?page=2&artist=The%20Beatles&song=",
        "https://www.songkeyfinder.com/search?page=3&artist=The%20Beatles&song=",
        "https://www.songkeyfinder.com/search?page=4&artist=The%20Beatles&song=",
        "https://www.songkeyfinder.com/search?page=5&artist=The%20Beatles&song=",
        "https://www.songkeyfinder.com/search?page=6&artist=The%20Beatles&song=",
    ]
    domain_name = 'https://www.songkeyfinder.com'

    for i in range(6):

        source = requests.get(pages[i]).text
        soup = BeautifulSoup(source, 'lxml')

        for a in soup.find_all('a', href=True):
            if a['href'].startswith('/songs'):
                link = domain_name + a['href']
                current_source = requests.get(link).text
                current_soup = BeautifulSoup(current_source, 'lxml')

                key = current_soup.find("h3").text
                title = current_soup.find("h2").text
                key = key[9:-1]
                title = title[:-14]

                csv_writer.writerow([title, key])

    csv_file.close()

# csv_from_inwhatkey()
# csv_from_SongKeyFinder()