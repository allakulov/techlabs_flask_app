import requests
from fastbook import *
from fastai.vision.widgets import *

def custom_search_images_bing(key, term, min_sz=128, max_images=150):
    params = dict(q=term, count=max_images, min_height=min_sz, min_width=min_sz)
    
    ## old url provided by fastai
    search_url = "https://api.bing.microsoft.com/v7.0/images/search"
    
    ## New url provided by microsoft
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    
    response = requests.get(search_url, headers={"Ocp-Apim-Subscription-Key":key}, params=params)
    response.raise_for_status()
    return L(response.json()['value'])