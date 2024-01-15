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

@app.route('/predict.html',methods=['POST'])
def predict_crop():
    Nitrogen=int(request.form.get('Nitrogen'))
    Phosphorous=int(request.form.get('Phosphorous'))
    Potassium=int(request.form.get('Potassium'))
    Temperature=float(request.form.get('Temperature'))
    Humidity=float(request.form.get('Humidity'))
  
    PH=float(request.form.get('PH'))
    Rainfall=float(request.form.get('Rainfall'))
    result=model.predict(np.array([Nitrogen,Phosphorous,Potassium,Temperature,Humidity,PH,Rainfall]).reshape(1,7))
    
    #return str(result)
    return render_template('predict.html', prediction=result )

#for fertilizer recomendation

@app.route('/predict1.html',methods=['POST'])
def predict_fertilizer():
    Nitrogen=int(request.form.get('Nitrogen'))
    Phosphorous=int(request.form.get('Phosphorous'))
    Potassium=int(request.form.get('Potassium'))
    Temperature=float(request.form.get('Temperature'))
    Humidity=float(request.form.get('Humidity'))
    Moisture=float(request.form.get('Moisture'))
    SoilType=int(request.form.get('SoilType'))
    CropType=int(request.form.get('CropType'))

    

    result=model2.predict(np.array([Temperature,Humidity,Moisture,SoilType,CropType,Nitrogen,Potassium,Phosphorous]).reshape(1,8))
    if result[0] == 0:
     return str("10-26-26")
    elif result[0] ==1:
     return str("14-35-14")
    elif result[0] == 2:
     return str("17-17-17	")
    elif result[0] == 3:
     return str("20-20")
    elif result[0] == 4:
     return str("28-28")
    elif result[0] == 5:
     return str("DAP")
    else:
     return str("Urea")
    
    return render_template('fertilizer.html', prediction=result)

if __name__=='__main__':
    app.run(debug=True)