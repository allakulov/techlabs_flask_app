# import necessary libraries
from flask import Flask, request, render_template, jsonify
from fastai.vision.all import *
from fastai.vision.widgets import *
from utils import mkdir_aftercheck

# define a flask app
app = Flask(__name__)

# assign model
MODEL_NAME = 'learner.pkl'

def model_predict(img_path, model_path):    
    learn_inf = load_learner(model_path)
    pred , pred_idx , probs = learn_inf.predict(img_path)    
    prob_value = probs[pred_idx] * 100     
    out = f'Our AI model thinks the item in your image is {pred} with {prob_value:.02f} % confidence.'
    return out

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

# create API
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = Path(__file__).parent
        file_path = basepath.joinpath('uploads')
        mkdir_aftercheck(file_path)
        filename = 'test.jpg'
        file_path = file_path.joinpath(filename)
        f.save(file_path)

        # Make prediction
        path = Path()
        model_path = (path/MODEL_NAME)
        out = model_predict(file_path, model_path)

        return out
    return None

if __name__ == '__main__':
    app.run(debug=True)