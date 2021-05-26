import fastbook
fastbook.setup_book()

from fastbook import *
from fastai.vision.widgets import *


def test_download():
    
    key = os.environ.get('AZURE_SEARCH_KEY')
    results = search_images_bing(key, 'dog')
    ims = results.attrgot('contentUrl')
    path = Path()
    print(path)
    o = 'images'
    
    dest_1 = (path/o)
    dest_1.mkdir(exist_ok = True)
    
    dest_2 = dest_1/'test_img.jpg'
    download_url(ims[0], dest_2)
    im = Image.open(dest_2)
    im.to_thumb(128,128)


def download_relevant_images(labels = ['cat','dog'] , label_name = 'animals'):
    
    key = os.environ.get('AZURE_SEARCH_KEY')
    
    data_path = Path("DATA")
    parent_path = (data_path/label_name)
    
    if not data_path.exists():
        data_path.mkdir()

    if not parent_path.exists():
        parent_path.mkdir()

    for i in labels :
        category = (parent_path/i)
        category.mkdir(exist_ok=True)
        results = search_images_bing(key, f'{i}')
        download_images(category, urls=results.attrgot('contentUrl'))
    
    return parent_path

def clean_label_images(path):
    fns = get_image_files(path)
    failed = verify_images(fns)
    failed.map(Path.unlink)

if __name__ == "__main__":
    label_path = download_relevant_images(labels = ['cat','dog'] , label_name = 'animals')
    clean_label_images(label_path)