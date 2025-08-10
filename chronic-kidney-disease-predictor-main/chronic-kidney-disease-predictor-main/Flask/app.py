from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('CKD.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    
    output = prediction[0]
    
    if output == 1:
        prediction_text = 'The person is likely to have Chronic Kidney Disease.'
    else:
        prediction_text = 'The person is not likely to have Chronic Kidney Disease.'

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)