import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('credit.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')




@app.route('/predict',methods=['POST'])
def predict():

    time=request.form['time']
    time=float(time)

    v1=request.form['v1']
    v1=float(v1)

    v2=request.form['v2']
    v2=float(v2)

    v3=request.form['v3']
    v3=float(v3)

    v4=request.form['v4']
    v4=float(v4)

    v5=request.form['v5']
    v5=float(v5)
    
    v6=request.form['v6']
    v6=float(v6)

    v7=request.form['v7']
    v7=float(v7)

    v8=request.form['v8']
    v8=float(v8)

    v9=request.form['v9']
    v9=float(v9)

    v10=request.form['v10']
    v10=float(v10)
    
    v11=request.form['v11']
    v11=float(v11)

    v12=request.form['v12']
    v12=float(v12)

    v13=request.form['v13']
    v13=float(v13)

    v14=request.form['v14']
    v14=float(v14)

    v15=request.form['v15']
    v15=float(v15)
    
    v16=request.form['v16']
    v16=float(v16)

    v17=request.form['v17']
    v17=float(v17)

    v18=request.form['v18']
    v18=float(v18)

    v19=request.form['v19']
    v19=float(v19)

    v20=request.form['v20']
    v20=float(v20)

    v21=request.form['v21']
    v21=float(v21)

    v22=request.form['v22']
    v22=float(v22)
    
    v23=request.form['v23']
    v23=float(v23)

    v24=request.form['v24']
    v24=float(v24)

    v25=request.form['v25']
    v25=float(v25)
    
    v26=request.form['v26']
    v26=float(v26)

    v27=request.form['v27']
    v27=float(v27)

    v28=request.form['v28']
    v28=float(v28)
    
   

    amount=request.form['amount']
    amount=float(amount)


    
    
    
    
   
    int_features = [time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,
    v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,
    v25,v26,v27,v28,amount]

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    

    return render_template('result.html', prediction_text='The Passenger {}'.format(prediction[0]),prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
    
    
