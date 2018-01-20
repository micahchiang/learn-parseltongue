#! /usr/bin/env python3
# downloads xkcd comics

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download Page
    print('Downloading page %s...'  % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    # Find URL of comic img
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('No comic found')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download img 
            print('Downloading img %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue

    # Save img
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get prev btn url
        prevLink = soup.select('a[rel="prev"]')[0]
print('Done.')