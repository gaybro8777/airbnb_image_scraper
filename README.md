# A scraper for Airbnb listing images
Let's say you want to do some image recognition on some Airbnb listings. However, there isn't currently that kind of image dataset (at least, I couldn't find one). This script should help you.

### Usage

**Step 1**:  
Fork this repo, then clone it somewhere onto your computer.

**Step 2**:  
Download a dataset containing Airbnb listing ID's. I used the Boston Airbnb Dataset (found [here](https://www.kaggle.com/airbnb/boston#listings.csv), just use listings.csv) for testing. However, any csv of listing ID's should work as long as you name the column 'id' for the ID column.

Put the csv file into the same directory as this python script. Then, rename it into 'listings.csv'.

**Step 3**:  
Run the python script by typing this into your terminal:  
```python airbnb_image_scraper.py [numListings] ```  
The numListings argument allows you to specify how many listings to scrape images for. For example, if I just wanted the images for the first 20 listings, I would write:
```python airbnb_image_scraper.py 20```

Cheers!
