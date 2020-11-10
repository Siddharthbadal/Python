import os
import json
import requests
from bs4 import BeautifulSoup


google_images = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
SAVE_FOLDER = 'images'


def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()


def download_images():
    data = input("what are you looking for.. ")
    n_images = int(input("How many images...  "))

    print('Searching for you images.... ..')

    searchurl = google_images + 'q=' + data
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('img', {'class': 'rg_i Q4LuWd'})
   
    count = 0
    imageLinks = []

    for result in results:
        try:
            imagelink = result['data-src']
            imageLinks.append(imagelink)
            count += 1
            if(count >= n_images):
                break

        except KeyError:
            continue

    print(f"Downloading {len(imageLinks)} images...")
    print("Downloading... ..")

    for i, imagelink in enumerate(imageLinks):
        response = requests.get(imagelink)

        imagename = SAVE_FOLDER + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('done')


if __name__ == '__main__':
    main()
