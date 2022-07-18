from __future__ import division, print_function
# coding=utf-8
# Flask utils
from flask import Flask, request, render_template, jsonify

# Define a flask app
app = Flask(__name__)

#
from fastai.vision.all import *
from fastai.vision.widgets import *
from utils import create_directory_if_not_exists

MODEL_NAME = 'learner.pkl'


print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model_path):
    
    learn_inf = load_learner(model_path)
    pred , pred_idx , probs = learn_inf.predict(img_path)
    
    prob_value = probs[pred_idx] * 100 
    
    out = f'Our machine learning model has predicted the image to be {pred} with {prob_value:.02f} % confidence !'

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

        return out
    return None

@app.route('/predictapi', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = Path(__file__).parent
        file_path = basepath.joinpath('uploads')
        create_directory_if_not_exists(file_path)
        filename = 'test.jpg'
        file_path = file_path.joinpath(filename)
        f.save(file_path)

        # Make prediction
        learn_inf = load_learner(model_path)
        pred , pred_idx , probs = learn_inf.predict(file_path)
        prob_value = probs[pred_idx] * 100 
        result = {'prediction': pred, 'probability': prob_value}

        return jsonify(result)
    return None

# @app.route('/predictapi',methods=['POST'])
# def predictapi():
#     '''
#     For rendering results on HTML GUI
#     '''
#     img = request.files.get('file')

#     if not img or not img.filename:
#         raise BadRequest("You need to upload a file")

#     basepath = Path(__file__).parent
#     file_path = basepath.joinpath('uploads')
#     create_directory_if_not_exists(file_path)
#     filename = 'test.jpg'
#     file_path = file_path.joinpath(filename)
#     img.save(file_path)    

#     path = Path()
#     model_path = (path/MODEL_NAME)
#     learn_inf = load_learner(model_path)
#     pred , pred_idx , probs = learn_inf.predict(file_path)
#     prob_value = probs[pred_idx] * 100 
#     result = {'prediction': pred, 
#     'probability': prob_value
#     }

#     return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)