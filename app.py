# References
# https://www.reddit.com/r/learnpython/comments/j57drt/building_a_web_based_app_using_python_and_flask/

from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

pickle_in = open('regressor.pkl','rb')
regressor = pickle.load(pickle_in)


@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = request.form['Years']
        num1 = float(num1)
        prediction = regressor.predict(np.reshape([num1],(-1,1)))        
    
    return render_template('app.html', sum='Employee Salary is : $ '+ str(round(prediction[0],2)))
       

if __name__=="__main__":  
   
    app.run(debug=True)

    
   
    