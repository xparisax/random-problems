import urllib.request
import bs4 as bs
import csv
import sys

file = csv.writer(open('news_title.csv', 'w'))
file.writerow(['titles'])

def get_page(page_number):
    site = 'https://www.reuters.com/news/archive/technologynews?view=page&page=' + str(page_number)
    return site
#int(sys.argv[1])
for i in range(int(sys.argv[1])):
    source = get_page(i)
    url = urllib.request.urlopen(source).read()
    soup = bs.BeautifulSoup(url, 'lxml')

    for title in soup.find_all('h3', class_='story-title'):
        file.writerow([title.text])
