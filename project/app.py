from flask import Flask, render_template, request
import analysis
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    barColors = ["red", "green","blue","orange","brown"];

    xValues, yValues = analysis.filter_by_time()
    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors)

@app.route("/submit", methods =["GET", "POST"])
def submit():

    barColors = ["red", "green","blue","orange","brown"];

    start = pd.to_datetime(request.form['start'])
    end = pd.to_datetime(request.form['end'])

    xValues, yValues = analysis.filter_by_time(start, end)
    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors)

if __name__ == '__main__':
    app.run(debug=True)

