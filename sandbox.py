from fastbook import *
from fastai.vision.widgets import *
from utils import create_directory_if_not_exists

MODEL_NAME = 'animals_prediction.pkl'

path = Path()
model_path = (path/MODEL_NAME)
    
learn_inf = load_learner(model_path)
pred , pred_idx , probs = learn_inf.predict(img_path)

out = f'Prediction:{pred} : probability: {probs[pred_idx]:.04f}'

# Save the file to ./uploads
basepath = Path(__file__).parent
file_path = basepath.joinpath('uploads')
create_directory_if_not_exists(file_path)
filename = 'test.jpg'
file_path = file_path.joinpath(filename)
f.save(file_path)

# Make prediction
path = Path()
model_path = (path/MODEL_NAME)
out = model_predict(file_path, model_path)


