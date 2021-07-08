from fastbook import *
from fastai.vision.widgets import *

MODEL_NAME = 'animals_prediction.pkl'

path = Path()
model_path = (path/MODEL_NAME)
    
learn_inf = load_learner(model_path)

img_path = (path/'uploads'/'test.jpg')
pred , pred_idx , probs = learn_inf.predict(img_path)

out = f'Prediction:{pred} : probability: {probs[pred_idx]:.04f}'

print(out)