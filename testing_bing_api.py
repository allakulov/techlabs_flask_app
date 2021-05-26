import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os

key = os.environ.get('AZURE_SEARCH_KEY')
subscription_key = os.environ.get('AZURE_SEARCH_KEY')

# New API
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
search_term = "puppies"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

params  = {"q": search_term, "license": "public", "imageType": "photo"}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]


f, axes = plt.subplots(4, 4)
for i in range(4):
    for j in range(4):
        image_data = requests.get(thumbnail_urls[i+4*j])
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))        
        axes[i][j].imshow(image)
        axes[i][j].axis("off")
plt.show()

min_sz=128
max_images=150

params = dict(q=search_term, count=max_images, min_height=min_sz, min_width=min_sz)

# Old API
search_url = "https://api.bing.microsoft.com/v7.0/images/search"
response = requests.get(search_url, headers={"Ocp-Apim-Subscription-Key":key}, params=params)
response.raise_for_status()
    
