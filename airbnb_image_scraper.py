import pandas as pd

import requests
import urllib.request

import sys
import pathlib
import timeit

def imageURLs(listing_id):
    """For each listing, grabs image URL's
    Args:
        listing ID (str): listing ID for a particular listing
    Returns: list of all image URL's for listing"""

    parameters = {'client_id': '3092nxybyb0otqw18e8nh5nty', '_format': 'v1_legacy_for_p3'}
    url = 'https://api.airbnb.com/v2/listings/' + str(listing_id)
    r = requests.get(url, params=parameters)

    if 'error_code' in r.text:
        return {listing_id: 'unlisted'}

    listing_info_df = pd.read_json(r.text)
    urls = listing_info_df['listing']['xl_picture_urls']
    output = {listing_id: urls}

    return output

def saveImages(url_dict):
    """Function to save images to a folder.
    Folder name is the listing ID.
    Each folder contains some images. These image names would be the listing id concatenated with a counter
    For instance, the 4th picture from listing 532134 would be named '532134_4.jpg', and would be stored
    in the folder named '532134' """

    for key in list(url_dict.keys()):
        print(key)
        c = 0 

        my_path = 'images/' + str(key)
        pathlib.Path(my_path).mkdir(parents=True, exist_ok=True)
        my_path = my_path + '/'
        if url_dict[key] == 'unlisted':
            continue
        for url in url_dict[key]:
            img_name = str(key) + '_' + str(c+1) + '.jpg'
            urllib.request.urlretrieve(url, my_path + img_name)
            c = c+1

def main():
    df = pd.read_csv('listings.csv')
    num_listings = int(sys.argv[1])
    ids = df['id'][0:num_listings]
    image_urls = {}

    print('Scraping images for the first', num_listings, 'listings')

    for i in ids:
        image_urls.update(imageURLs(i))

    start_time = timeit.default_timer()
    saveImages(image_urls)
    elapsed = timeit.default_timer() - start_time

    print('Elapsed time for 10 listings: ' + str(elapsed))

if __name__ == '__main__':
    main()
