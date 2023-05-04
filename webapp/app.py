# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 00:10:36 2023

@author: DELL
"""

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

dic = {0 : 'bacterial_blight', 1 : 'curl_virus', 2 : 'fussarium_wilt',3 : 'healthy'}

model = load_model("D:\Projects\Cotton Plant Disease Project\webapp\swin_transformer.h5")

model.make_predict_function()

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224,224))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1, 224,224,3)
    p = model.predict(i)
    predicted_class = np.argmax(p, axis=1)
    return dic[predicted_class[0]]

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']
		img_path = "static/" + img.filename
		img.save(img_path)
		p = predict_label(img_path)
	return render_template("index.html", prediction=p, img_path=img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)