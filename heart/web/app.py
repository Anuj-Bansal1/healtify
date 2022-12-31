
from flask import Flask,render_template,request
import numpy as np
from tensorflow import keras
import tensorflow as tf

model= keras.models.load_model(r'C:\Users\HP\Desktop\projects\heart\web\models\health_model.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    tf.config.run_functions_eagerly(True)
    x=[float(i) for i in request.form.values()]
    
    
    predict = model.predict([x])
    final= (predict[0][0])*100
    output = round(final,2)
    return render_template('index.html', prediction_text = 'your healtify score is {}'.format(output))

if __name__ == '__main__':
    app.run()