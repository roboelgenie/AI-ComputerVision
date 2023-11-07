"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

# pip install google_images_download
from google_images_download import google_images_download

# Wszytskie argumenty funkcji download() dostępne pod linkiem:
# https://google-images-download.readthedocs.io/en/latest/arguments.html

# https://chromedriver.chromium.org/downloads

response = google_images_download.googleimagesdownload()

search_querries = ['horse', 'lion']


def download_images(query):
    arguments = {
        'keywords': 'horse',
        'format': 'jpg',
        'limit': 30,
        'size': 'medium',
        'aspect_ratio': 'square',

    }

    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {
            'keywords': 'horse',
            'format': 'jpg',
            'limit': 3,
            'size': 'medium',

        }
        try:
            response.download(arguments)
        except:
            pass


for query in search_querries:
    download_images(query)
    print()