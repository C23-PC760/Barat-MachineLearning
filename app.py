import os
import sys
import tensorflow as tf
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from src.handler import predict_handler



load_dotenv() # Load enviroment variable
sys.path.append(os.getcwd()) # adding current working directory (i.e) root folder of the project to the PATH
tf_model = tf.keras.models.load_model('src/model/model.h5', compile=False) # Load ML Model



app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def run_predict():
    # =====================[ authentication ]===================
    header_token = request.headers.get('X-Auth-Token')
    if(os.environ["API_KEY"] != header_token ):
        return jsonify({
            'error': True,
            'message': 'Failed',
            'result': "Api Key tidak Sesuai"
        }), 400
    
    # =====================[ predict image ]=====================
    uploaded_file = request.files['file']
    result = predict_handler(tf_model, uploaded_file)
    
    return jsonify({
        'error': False,
        'message': 'Success',
        'result': result
    }), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)