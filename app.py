
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['sex'])    
   inputs.append(request.form['cp'])
   inputs.append(request.form['trestbps'])
   inputs.append(request.form['chol'])
   inputs.append(request.form['fbs'])
   inputs.append(request.form['restecg'])
   inputs.append(request.form['thalach'])
   inputs.append(request.form['exang'])
   inputs.append(request.form['oldpeak'])
   inputs.append(request.form['slope'])
   inputs.append(request.form['ca'])
   inputs.append(request.form['thal'])

   
   class1 = request.form['age']
   gender = request.form['sex'] 
   siblings = request.form['cp']
   embarked = request.form['trestbps']
   embarked = request.form['chol']
   embarked = request.form['fbs']
   embarked = request.form['restecg']
   embarked = request.form['thalach']
   embarked = request.form['exang']
   embarked = request.form['oldpeak']
   embarked = request.form['slope']
   embarked = request.form['ca']
   embarked = request.form['thal']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = 1
   if prediction[0] == 0:
        categorical_array = 0
    
   result= categorical_array
   
       
   return render_template('Home.html', prediction_text1=result)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)