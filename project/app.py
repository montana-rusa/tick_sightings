from flask import Flask, render_template, request, redirect
import analysis
import pandas as pd

app = Flask(__name__)

start, end, location = None


@app.route("/")
def home():

    barColors = ["red", "green","blue","orange","brown"];

    xValues, yValues = analysis.filter_by_time()
    xValues2, yValues2 = analysis.filter_by_location()



    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors, xValues2 = xValues2, yValues2 = yValues2)

@app.route("/submit1", methods =["GET", "POST"])
def submit1():

    if request.method == "GET":
        return redirect("/")

    barColors = ["red", "green","blue","orange","brown"];

    start = pd.to_datetime(request.form['start'])
    end = pd.to_datetime(request.form['end'])

    xValues, yValues = analysis.filter_by_time(start, end)
    xValues2, yValues2 = analysis.filter_by_location()

    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors, xValues2 = xValues2, yValues2 = yValues2)

if __name__ == '__main__':
    app.run(debug=True)

