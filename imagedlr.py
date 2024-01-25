import requests
import pandas as pd
import os
from urllib.parse import urlparse

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Load the CSV file
df = pd.read_csv('options.csv')

if not os.path.exists('images'):
    os.makedirs('images')

# Assuming the URLs are in a column named 'url'
for index, row in df.iterrows():
    url = row['url']
    # Parse the url to get the image extension
    parsed_url = urlparse(url)
    image_ext = os.path.splitext(parsed_url.path)[1]
    
    # Use the index or another column to create a unique filename for each image
    filename = os.path.join('images', f'image_{index}{image_ext}')
    download_image(url, filename)
