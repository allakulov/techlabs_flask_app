import fastbook
fastbook.setup_book()

from fastbook import *
from fastai.vision.widgets import *

MODEL_NAME = 'animals_prediction.pkl'

path = Path()
model_path = (path/MODEL_NAME)
    
learn_inf = load_learner(model_path)

import torchvision.transforms as tfms

def pil2fast(img):  
  return Image(tfms.ToTensor()(img))

img = PILImage.create('uploads/test.jpg')
image2tensor(img)
pred , pred_idx , probs = learn_inf.predict(img)

out = f'Prediction:{pred} : probability: {probs[pred_idx]:.04f}'

print(out)

