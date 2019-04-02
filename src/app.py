from flask import Flask, render_template, url_for, request
import numpy as np
from sklearn.externals import joblib
import re

app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run


@app.route('/', methods=['POST', 'GET'])
def home():
    clf = joblib.load(open('fakenews_model.pkl', 'rb'))

    if request.method == 'POST':
        content = request.form['content']
        content = format_string(content)
        content = [content]
        content = np.array(content)
        pred = clf.predict(content)
        pred = '#F44336' if pred else '#4CAF50'
        return render_template('home.html', pred=pred)
    else:
        pred = 'white'
        return render_template('home.html', pred=pred)


def format_string(s):
    return re.sub(r'\W+', ' ', s)


if __name__ == '__main__':
    #	app.run(debug=True)
    app.run()
