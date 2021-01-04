from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('songs_data.csv', 'w')
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
