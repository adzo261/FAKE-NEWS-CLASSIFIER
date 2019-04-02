from flask import Flask,render_template,url_for,request
from flask_ngrok import run_with_ngrok
import numpy as np
import pickle
from sklearn.externals import joblib
import re

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
#	joblib.dump(clf, 'fakenews_model.pkl')
	model = open('fakenews_model.pkl','rb')
	clf = joblib.load(model)

	if request.method == 'POST':
		message = request.form['message']
		message = [message]
#		check_test=np.array(news_list)
#		data = cv.transform(data).toarray()
#		message = re.sub(r'\W+', ' ', message)
		message = np.array(message)
		my_prediction = clf.predict(message)
	return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
#	app.run(debug=True)
	app.run()


"""
check_test=np.array(news_list)
def format_string(s):
    return re.sub(r'\W+', ' ', s)

"""