from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

#
from fastbook import *
from fastai.vision.widgets import *



MODEL_NAME = 'animals_prediction.pkl'


print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model_path):
    
    learn_inf = load_learner(model_path)
    pred , pred_idx , probs = learn_inf.predict(img_path)
    
    out = f'Prediction:{pred} : probability: {probs[pred_idx]:.04f}'

    return out


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        path = Path()
        model_path = (path/MODEL_NAME)
        out = model_predict(file_path, model_path)

        return out
    return None


if __name__ == '__main__':
    app.run(debug=True)