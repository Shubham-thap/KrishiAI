from flask import Flask,render_template, request
import pickle

import numpy as np 
model=pickle.load(open('model.pkl','rb'))
model2=pickle.load(open('model2.pkl','rb'))
 
app = Flask(__name__)

@ app.route('/')
def index():
    title = 'Krishi-AI'
    return render_template('index.html', title=title)
@ app.route('/home.html')
def home():
    title = 'Krishi-AI'
    return render_template('/home.html', title=title)
@ app.route('/contact.html')
def contact():
    title = 'Krishi-AI Contact'
    return render_template('contact.html', title=title)

@ app.route('/crop.html')
def crop():
    title = 'KrishiAI- Crop Recommendation'
    return render_template('crop.html', title=title)

@ app.route('/insecticide.html')
def insecticide():
    title = 'KrishiAI- Insecticide'
    return render_template('insecticide.html', title=title)

@ app.route('/predict.html')
def predict():
    title = 'KrishiAI- Prediction'
    return render_template('predict.html', title=title)
@ app.route('/predict1.html')
def predict1():
    title = 'KrishiAI- Prediction'
    return render_template('predict1.html', title=title)

@ app.route('/predict2.html')
def predict2():
    title = 'KrishiAI- Prediction'
    return render_template('predict2.html', title=title)

@ app.route('/service.html')
def service():
    title = 'KrishiAI- Service'
    return render_template('service.html', title=title)

@ app.route('/fertilizer.html')
def fertilizer():
    title = ' KrishiAI- Fertilizer Suggestion'

    return render_template('fertilizer.html', title=title)

@app.route('/predict.html', methods=['POST'])
def predict_crop():
    if request.method == 'POST':
        # Retrieve form values with default value of 0 if not provided
        Nitrogen = int(request.form.get('Nitrogen', 0))
        Phosphorus = int(request.form.get('Phosphorus', 0))
        Potassium = int(request.form.get('Potassium', 0))
        Temperature = float(request.form.get('Temperature', 0.0))
        Humidity = float(request.form.get('Humidity', 0.0))
        PH = float(request.form.get('PH', 0.0))
        Rainfall = float(request.form.get('Rainfall', 0.0))

        result = model.predict(np.array([Nitrogen, Phosphorus, Potassium, Temperature, Humidity, PH, Rainfall]).reshape(1, 7))
        print("Predicted Result:", result)
        return render_template('predict.html', value=result[0])
    else:
        return render_template('try_again.html', message='Invalid request method')


# for fertilizer recomendation

@app.route('/predict1.html', methods=['POST'])
def predict_fertilizer():
    if request.method == 'POST':
        Nitrogen = int(request.form.get('Nitrogen', 0))
        Phosphorous = int(request.form.get('Phosphorus', 0))
        Potassium = int(request.form.get('Potassium', 0))
        Temperature = float(request.form.get('Temperature', 0.0))
        Humidity = float(request.form.get('Humidity', 0.0))
        Moisture = float(request.form.get('Moisture', 0.0))
        SoilType = int(request.form.get('SoilType', 0))
        CropType = int(request.form.get('CropType', 0))

        result1 = model2.predict(np.array([Temperature, Humidity, Moisture, SoilType, CropType, Nitrogen, Potassium, Phosphorous]).reshape(1, 8))

        predicted_fertilizer = ""
        if result1[0] == 0:
            predicted_fertilizer = "10-26-26"
        elif result1[0] == 1:
            predicted_fertilizer = "14-35-14"
        elif result1[0] == 2:
            predicted_fertilizer = "17-17-17"
        elif result1[0] == 3:
            predicted_fertilizer = "20-20"
        elif result1[0] == 4:
            predicted_fertilizer = "28-28"
        elif result1[0] == 5:
            predicted_fertilizer = "DAP"
        else:
            predicted_fertilizer = "Urea"

        return render_template('predict1.html', str=predicted_fertilizer)
    else:
        return render_template('try_again.html', message='Invalid request method')



if __name__ == '__main__':
    app.run(debug=True)
